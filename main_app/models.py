from django.db import models
from django.db.models.fields import TextField

# Create your models here.
class MessageForm(models.Model):
    name = models.CharField(max_length=300 , default= None)
    email = models.EmailField()
    phone_no = models.CharField(max_length=20 , default= None)
    MessageForm = models.TextField()
