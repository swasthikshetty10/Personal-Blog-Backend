
from .blog import *
from .contact import *
from .projectreq import *
from rest_framework import generics


class apioverview(generics.GenericAPIView):
    
    # queryset = ContactForm.objects.all()
    pass
    
    # def post(self ,request , *args , **kwargs):
    #     print(request.data)
    #     return self.create(request, *args, **kwargs)
    # def get_serializer(self, instance=None, data=None, many=False, partial=False):
    #     print(data)
    
    