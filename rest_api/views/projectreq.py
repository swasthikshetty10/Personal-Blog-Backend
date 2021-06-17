from django.http import request
from rest_framework import generics
from rest_framework.serializers import Serializer
from main_app.models import ContactForm
from rest_api.serializers import ContactSerializer
from rest_framework.response import Response
from rest_framework import status
import smtplib 
from core.settings import env

class projectreq(generics.GenericAPIView):
    
    # queryset = ContactForm.objects.all()
    pass
    
    # def post(self ,request , *args , **kwargs):
    #     print(request.data)
    #     return self.create(request, *args, **kwargs)
    # def get_serializer(self, instance=None, data=None, many=False, partial=False):
    #     print(data)
    
    