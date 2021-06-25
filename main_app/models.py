from django.db import models
from django.db.models.fields import TextField
from django.utils import timezone
from django.contrib.auth.models import User
from main_app.Utility.formatChecker import ContentTypeRestrictedFileField
from django.template.defaultfilters import slugify
class ContactForm(models.Model):
    name = models.CharField(max_length=300 , default= None)
    email = models.EmailField()
    phone_no = models.CharField(max_length=20 , default= None)
    message= models.TextField()
    time = models.DateTimeField(default=timezone.now)
    def __str__(self) -> str:
        return self.name


def get_filename(instance, filename):
    title = instance.post.title
    slug = slugify(title)
    return "files/%s-%s" % (slug, filename)  
class ProjectRequests(models.Model):
    user = models.ForeignKey(User , on_delete = models.CASCADE , null = True)
    projectName = models.TextField()
    projectDescription = models.TextField()
    orderDate = models.DateTimeField(default=timezone.now)
    amountType = models.IntegerField(default=0)
    projectBudget = models.FloatField()
    finalDate = models.DateTimeField()
    files = ContentTypeRestrictedFileField( content_types=['video/x-msvideo', 'application/pdf', 'video/mp4', 'audio/mpeg','image/jpeg' ] ,max_upload_size=20971520 , blank=True, null=True)
