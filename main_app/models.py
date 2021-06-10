from django.db import models
from django.db.models.fields import TextField
from django.utils import timezone
# Create your models here.
class ContactForm(models.Model):
    name = models.CharField(max_length=300 , default= None)
    email = models.EmailField()
    phone_no = models.CharField(max_length=20 , default= None)
    message= models.TextField()
    time = models.DateTimeField(default=timezone.now)
    def __str__(self) -> str:
        return self.name
