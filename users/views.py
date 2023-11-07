from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login,logout
from users.models import Student,Teacher
# Create your views here.

def login_view(request):
    if request.user.is_authenticated:
        stud=Student.objects.filter(id=request.user.id).first()
        teach=Teacher.objects.filter(id=request.user.id).first()
        if stud is not None:
            return  redirect('proj1-dashboard')
        else:
            return redirect('add_exam')
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()

            if user is not None:
                
                login(request,user)
                stud=Student.objects.filter(id=request.user.id).first()
                teach=Teacher.objects.filter(id=request.user.id).first()
                if stud is not None:
                    return redirect('proj1-dashboard')
                elif teach is not None:
                    return redirect('add_exam')
                else :
                    return redirect('proj1-details')
    else:
        form=AuthenticationForm()
    return render(request,'users/login.html',{'form':form})

def register_view(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users-login')
            
    else:
        form=UserCreationForm()
    return render(request,'users/register.html',{'form':form})

def logout_view(request):
    if request.method=='POST':
        logout(request)
        return redirect('proj1-form')