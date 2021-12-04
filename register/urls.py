from django.urls import path
from . import views


""" Url Pattern for root URL Pattern """
urlpatterns = [
    path('home',views.home,name='home'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('logout',views.logout,name='logout')

   
]