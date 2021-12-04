from django.contrib import admin
from . models import user_profile

# Register your models here.
class user_profileAdmin(admin.ModelAdmin):
    list_display=['user','profile_picture','mobile_no','address']

admin.site.register(user_profile, user_profileAdmin)