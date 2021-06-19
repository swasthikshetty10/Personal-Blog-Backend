
from .blog import *
from .contact import *
from .projectreq import *
from rest_framework.decorators import api_view

@api_view(['GET'])
def apioverview(request):
    
    return Response({
        "API_Routes": {
        "contact" : "/contact",
        "login" : "/login",
        "project_request" : "/projectrequest",
    }})
    