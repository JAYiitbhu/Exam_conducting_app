
#url file for the proj1 web app 
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name='proj1-home'),
    path('proj1/',views.home_page,name='proj1-form'),
    path('proj1/dashboard',views.dashboard,name='proj1-dashboard'),
    path('proj1/exam/',views.exam,name='proj1-exam'),
    path('proj1/report/',views.report,name='proj1-report'),
    path('proj1/save_details',views.save_profile,name='proj1-details'),
    path('profile/<int:id>',views.profile,name='proj1-profile'),
    path('quiz/<int:quiz_id>/', views.start_quiz, name='quiz_page'),
    path('quiz/<int:quiz_id>/update_score/', views.update_score, name='update_score'), # type: ignore
    path('proj1/teacher/add_exam',views.add_exam,name='add_exam'),
    path('quiz/<int:quiz_id>/add_question/<int:number>',views.add_ques,name='add_ques') # type: ignore

]
