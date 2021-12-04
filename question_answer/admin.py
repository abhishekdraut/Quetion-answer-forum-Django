from django.contrib import admin
from . models import Question, Answer

""" QuestionAdmin Admin Class : To change the default behavior of Django Adminstration """
class QuestionAdmin(admin.ModelAdmin):
    #list_display is used to add columns of model attributes to Django adminstration table view of app model
    # question, category, status and added_date will displayed as table columns
    list_display = ['question', 'category', 'status', 'added_date']
    #list_filter is used to add filters for columns of model attributes to Django adminstration table view of app model
    # status and added_date will act as filter to filter the data
    list_filter = ('status', 'added_date')
    

""" AnswerAdmin Admin Class : To change the default behavior of Django Adminstration"""
class AnswerAdmin(admin.ModelAdmin):
    #list_display is used to add columns of model attributes to Django adminstration table view of app model
    # question, answer, added_date, up_voting and down_vote will displayed as table columns
    list_display = ['question', 'answer', 'added_date', 'up_voting', 'down_vote']
    
    
"""
    Register App to Django Admin by passing model name as 1st parameter 
    admin.site.register(MODEL_NAME)    
    2nd paramter is option, if you want to change the default behavior of Django Admin then write a class and pass the class as 2nd parameter.
"""
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
