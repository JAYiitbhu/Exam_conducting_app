from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('login/',views.login_view,name='users-login'),
    path('signin/',views.register_view,name='users-register'),
    path('logout/',views.logout_view,name="users-logout") # type: ignore
]
