from django.contrib import admin
from . models import Category


""" 
    Category Admin Class : To change the default behavior of Django Adminstration
"""
class CategoryAdmin(admin.ModelAdmin):
    #list_display is used to add columns of model attributes to Django adminstration table view of app model
    # title and status will displayed as table columns
    list_display = ['title', 'status']
    
"""
    Register App to Django Admin by passing model name as 1st parameter 
    admin.site.register(MODEL_NAME)    
    2nd paramter is option, if you want to change the default behavior of Django Admin then write a class and pass the class as 2nd parameter.
"""
admin.site.register(Category, CategoryAdmin)