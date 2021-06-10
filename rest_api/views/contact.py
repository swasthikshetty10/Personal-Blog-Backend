from django.http import request
from rest_framework import generics
from rest_framework.serializers import Serializer
from main_app.models import ContactForm
from rest_api.serializers import ContactSerializer
from rest_framework.response import Response
from rest_framework import status
import smtplib 
from core.settings import env
def sendEmail(to, content): 
    try : 
        server  = smtplib.SMTP('smtp.gmail.com', 587) 
        server.ehlo() 
        server.starttls() 
        global env
        # Enable low security in gmail 
        email = env('EMAIL')
        passwd = env('PASSWORD')
        server.login(email,passwd ) 
        server.sendmail(email, to, content) 
        server.close()
        print("Email Sent!!")
    except Exception as error:
        print(error)
        pass

class contact(generics.CreateAPIView):
    # queryset = ContactForm.objects.all()
    serializer_class = ContactSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        print(serializer.data)
        sendEmail('swasthikshetty10902@gmail.com' ,
         f'''
         email : {serializer.data['email']} 
         name : {serializer.data['name']}
         phone_no :  {serializer.data['phone_no']}
         msg : {serializer.data['message']}
         ''')
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    # def post(self ,request , *args , **kwargs):
    #     print(request.data)
    #     return self.create(request, *args, **kwargs)
    # def get_serializer(self, instance=None, data=None, many=False, partial=False):
    #     print(data)
    
    