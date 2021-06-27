from django.db import models
from django.utils import timezone
from users.models import User
from main_app.Utility.formatChecker import ContentTypeRestrictedFileField

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
    projectDescription = models.TextField()
    orderDate = models.DateTimeField(default=timezone.now)
    amountType = models.IntegerField(default=0)
    projectBudget = models.FloatField()
    finalDate = models.DateTimeField()
    files = ContentTypeRestrictedFileField(upload_to = "files/", content_types=['video/x-msvideo', 'application/pdf', 'video/mp4', 'audio/mpeg','image/jpeg' ] ,max_upload_size=20971520 , blank=True, null=True)
