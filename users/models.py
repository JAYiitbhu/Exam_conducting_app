from django.db import models

# Create your models here.
class Student(models.Model):
    id=models.IntegerField(primary_key=True)
    Name=models.CharField(max_length=30)
    Address=models.TextField()
    last_visited=models.DateField(auto_now_add=True)
    country=models.CharField(max_length=15)
    

class Teacher(models.Model):
    id=models.IntegerField(primary_key=True)
    Name=models.CharField(max_length=30)
    Address=models.TextField()
    last_visited=models.DateField(auto_now_add=True)
    country=models.CharField(max_length=15)


class Teach_history(models.Model):
    tid=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    Exam_name=models.CharField(max_length=20)
    Maxscore=models.IntegerField()
    course=models.CharField(max_length=10)
    
class Stud_history(models.Model):
    sid=models.ForeignKey(Student,on_delete=models.CASCADE)
    Exam_name=models.CharField(max_length=20)
    Examid=models.ForeignKey(Teach_history,on_delete=models.CASCADE)
    Score=models.IntegerField()

class Teach_course(models.Model): 
    tid=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    course=models.CharField(max_length=10)

class Stud_course(models.Model): 
    sid=models.ForeignKey(Student,on_delete=models.CASCADE)
    course=models.CharField(max_length=10)

class Question(models.Model):
    text=models.TextField()
    examid=models.ForeignKey(Teach_history,on_delete=models.CASCADE)

class Chocies(models.Model): 
    text=models.TextField()
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    is_correct=models.BooleanField(default=False)

