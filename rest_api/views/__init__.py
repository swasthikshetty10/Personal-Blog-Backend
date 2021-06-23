
from .blog import *
from .contact import *
from .projectreq import *
from rest_framework.decorators import api_view ,  permission_classes
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def apioverview(request):
    
    return Response({
        "API_Routes": {
        "contact" : "/contact",
        "login" : "/login",
        "project_request" : "/projectrequest",
    }})
    