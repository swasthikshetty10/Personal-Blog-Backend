
from django.urls import path , include
from .views import *
urlpatterns = [
    path('contact/' , contact.as_view()  , name= "Contact"),
    path('projectrequest/' , projectreq.as_view()  , name= "projectrequest"),
   
]