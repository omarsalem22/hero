from django.urls import path
from .views import *

urlpatterns=[
    path('listapi',Booklistapi.as_view(),name="listapi")

 
]