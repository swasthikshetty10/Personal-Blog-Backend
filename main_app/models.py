from django.db import models
from django.db.models.fields import TextField
from django.utils import timezone
from django.contrib.auth.models import User

class ContactForm(models.Model):
    name = models.CharField(max_length=300 , default= None)
    email = models.EmailField()
    phone_no = models.CharField(max_length=20 , default= None)
    message= models.TextField()
    time = models.DateTimeField(default=timezone.now)
    def __str__(self) -> str:
        return self.name


class ProjectRequests(models.Model):
    user = models.ForeignKey(User , on_delete = models.CASCADE , null = True)
    projectName = models.TextField()
    orderDate = models.DateTimeField(default=timezone.now)

