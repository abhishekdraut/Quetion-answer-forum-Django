from django.db import models


""" Question Category Model Class """
class Category(models.Model):
    title = models.CharField(max_length=255)
    status = models.BooleanField(default=True)
    
    """ 
        Return a object representation string. Model Object PK to Category Title. 
        example Category Object (1) to Movies 
    """
    def __str__(self):
        return str(self.title)