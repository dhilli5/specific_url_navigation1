from django.urls import path
from app2.views import *
app_name="app2"
urlpatterns=[
    
path('rohit/',rohit,name='rohit'),
path('sachin/',sachin,name='sachin'),
]