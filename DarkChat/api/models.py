from django.db import models

# Create your models here.
class User_code(models.Model):
    '''
    Dark chat users database model
    '''

    username_code = models.CharField(max_length=25, unique=True)
    username_code_pass = models.CharField(max_length=50)

    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)



class messages(models.Model):
    '''
    user messages database model
    '''

    message_text = models.TextField()

    sender_user = models.ForeignKey("User_code", on_delete=models.CASCADE, related_name="sender")
    receiver_user = models.ForeignKey("User_code", on_delete=models.CASCADE, related_name="receiver")

    date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    