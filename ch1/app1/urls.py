from django.contrib import admin
from django.urls import path
from app1 import views as ap1


urlpatterns = [
    path('admin/', admin.site.urls),
    path('myfun/', ap1. myfunction, name=' myfunction'),
     path('app1/', ap1. home, name='home'),
    


]
