from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class user_profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    profile_picture=models.ImageField(null=True, blank=True)
    address=models.TextField(null=True,blank=True)
    mobile_no=models.CharField(max_length=10)
    
    
    def __str__(self):
        return str(self.user)
