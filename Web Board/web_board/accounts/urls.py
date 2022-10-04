from django.urls import path
from .views import Userregister

urlpatterns =[ 
     path('create', Userregister.as_view(), name='create'),
    ]
