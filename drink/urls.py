from django.urls import path
from drink.views import *

app_name ='drink'

urlpatterns = [
    path('oldmonk/', oldmonk, name='oldmonk'),
    path('redlabel/', redlabel, name='redlabel'),
]