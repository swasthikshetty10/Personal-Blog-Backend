
from django.db.models import fields
from main_app.models import ContactForm
from rest_framework import serializers
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactForm
        fields = ('id', 'name' , 'email' , 'phone_no' , 'message' )

