from django.contrib import admin
from course1.views import course1
from django.urls import path

urlpatterns = [
    
    path("course1/",course1)
]
