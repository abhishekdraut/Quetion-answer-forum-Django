from django.urls import path
from . import views

""" Url Pattern for root URL Pattern """
urlpatterns = [
    path('',views.homePage,name='home_page'),
    path('home',views.homePage,name='homepagestart'),
    path('category/<int:cat_id>',views.category_questions,name='category_question'),
    path('questions_details/<int:que_id>',views.questions,name='questions_ref'),
    path('comment_uploadation',views.comment_save,name="comment_save")
    
]
