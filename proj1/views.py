from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,Http404,JsonResponse
from django.contrib.auth.decorators import login_required
from users.models import Teacher,Student,Stud_history,Question,Chocies,Teach_history

def home(request):
    return HttpResponse('''<h1>mera website hai<br/> ye khol ke dekha</h1>
                            <a href="/proj1">click this</a>
                            
                        ''')

def home_page(request):
    return render(request,'proj1/home.html')
@login_required
def profile(request):
    context={}
    return render(request,"proj1/profile.html",context)
@login_required
def dashboard(request):

    attempt_exam=[]

    stud=Student.objects.get(pk=request.user.id)
    for x in Teach_history.objects.all():
        tmp=Stud_history.objects.filter(Examid=x,sid=stud).first()
        if tmp is not None:
            attempt_exam.append(x)
    return render(request,'proj1/dashboard.html',{'attempt_exam':attempt_exam})

@login_required
def save_profile(request):
    stud=Student.objects.filter(id=request.user.id).first()
    teach=Teacher.objects.filter(id=request.user.id).first()
    context={
        "address":"",
        "country":"",
        "stat":"student"
    }
    if request.method=="POST": 
        address=request.POST['address']
        c=request.POST['country']
        if teach is None and stud is None:
            stat=request.POST['stat']
            user=request.user
            if stat=="teacher":
                Teacher.objects.create(
                    id=user.id,Name=user.username,
                    Address=address,country=c
                )
                return redirect('add_exam')
            else: 
                Student.objects.create(
                    id=user.id,Name=user.username,
                    Address=address,country=c
                )
                return redirect('proj1-dashboard')
        elif teach is not None:
            teach.Address=address
            teach.country=c
            teach.save()
            return redirect('add_exam')
        elif stud is not None:
            stud.Address=address
            stud.country=c
            stud.save()

        
            return redirect('proj1-dashboard')
    elif teach is not None : 
        context["address"]=teach.Address
        context["country"]=teach.country
        context["stat"]="teacher"
    elif stud is not None: 
        context["address"]=stud.Address
        context["country"]=stud.country
    else:
        context["stat"]=""
    return render(request,"proj1/save_profile.html",context)


@login_required
def start_quiz(request, quiz_id):
    quiz = Teach_history.objects.get(pk=quiz_id) 
    questions = Question.objects.filter(examid=quiz)
    st=Student.objects.get(pk=request.user.id)
    if Stud_history.objects.filter(sid=st,Examid=quiz).first()is None:
        stud_quiz=Stud_history(sid=st,Exam_name=quiz.Exam_name,Examid=quiz,Score=0)
        stud_quiz.save()
    ques=[]
    for question in questions:
        tmp=[]
        for x in Chocies.objects.filter(question=question):
            d={
                'text':x.text,
                'id':x.id # type: ignore
            }
            tmp.append(d)
        d={
            'question':question,
            'choices':tmp
        }
        ques.append(d)
    return render(request, 'proj1/questions.html', {'quiz': quiz, 'ques': ques})


@login_required # type: ignore
def update_score(request, quiz_id):
    if request.method == "POST":
        quiz = get_object_or_404(Teach_history, pk=quiz_id)
        selected_choices = request.POST
        # Calculate the score based on the selected choices
        score = 0
        for i in range(1,quiz.Maxscore+1):
            choice = get_object_or_404(Chocies, pk=int(selected_choices[str(i)]))
            if choice.is_correct:
                score += 1
    
        st=Student.objects.get(pk=request.user.id)
        stud_quiz=Stud_history.objects.get(sid=st,Examid=quiz)
        stud_quiz.Score=score
        stud_quiz.save()
        return HttpResponse('''<h1>score:'''+str(score)+'''</h1>
                            <a href="/proj1/dashboard">go to dashboard</a>
                            
                        ''')
    else:
        return Http404(request)
    
@login_required
def add_exam(request):
    teach=Teacher.objects.filter(id=request.user.id).first()

    if teach is None:
        #go to dashboard with notification of only teachers
        redirect('proj1-dashboard')
        
    if request.method=='POST':
        #add exam details in teach_history
        exam_name=request.POST['exam_name']
        maxscore=request.POST['max_score']
        course=request.POST['course']
        quiz=Teach_history(tid=teach,Exam_name=exam_name,Maxscore=maxscore,course=course)
        quiz.save()
        quiz_id=quiz.id # type: ignore
        return redirect('/quiz/'+str(quiz_id)+'/add_question/1')
    return render(request,'proj1/add_exam.html')


@login_required # type: ignore
def add_ques(request,quiz_id,number):
    quiz=Teach_history.objects.filter(pk=quiz_id).first()
    if quiz is None: 
        return Http404(request)
    if request.method=="POST": 
        number+=1
        
        ques=Question(text=request.POST['question'],examid=quiz)
        ques.save()
        ans=request.POST['ans']
        for i in range(1,4):
            Chocies.objects.create(text=request.POST['choice-'+str(i)],question=ques,is_correct=(i==int(ans)))
        
        return redirect('/quiz/'+str(quiz_id)+'/add_question/'+str(number))
    return render(request,'proj1/add_ques.html',{'quiz':quiz,'number':number})

@login_required
def exam(request):
    exam=[]

    stud=Student.objects.get(pk=request.user.id)
    for x in Teach_history.objects.all():
        tmp=Stud_history.objects.filter(Examid=x,sid=stud).first()
        if tmp is None:
            exam.append(x)
    return render(request,'proj1/exam.html',{'exam':exam})
@login_required
def report(request):
    exam=[]

    stud=Student.objects.get(pk=request.user.id)
    for x in Teach_history.objects.all():
        tmp=Stud_history.objects.filter(Examid=x,sid=stud).first()
        if tmp is not None:
            exam.append(tmp)
    print(exam)
    return render(request,'proj1/report.html',{'exam':exam})