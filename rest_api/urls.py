
from django.urls import path , include
from .views import *
urlpatterns = [
    path('/' , apioverview.as_view()  , name= "Over_View"),
    path('contact/' , contact.as_view()  , name= "Contact"),
    path('projectrequest/' , projectreq.as_view()  , name= "projectrequest"),
   
]