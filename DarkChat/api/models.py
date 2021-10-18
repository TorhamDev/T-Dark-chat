from django.db import models

# Create your models here.
class User_code(models.Model):
    '''
    Dark chat users database model
    '''

    username_code = models.CharField(max_length=25, unique=True)
    username_code_pass = models.CharField(max_length=50)


    def __str__(slef) -> str:

        return slef.username_code
    