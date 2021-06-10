from rest_framework import generics
from main_app.models import ContactForm
from .serializers import ContactSerializer

class contact(generics.CreateAPIView):
    queryset = ContactForm.objects.all()
    serializer_class = ContactSerializer
    print("\n test  \n")

    pass
    