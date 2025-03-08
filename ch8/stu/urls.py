
from django.urls import path
from stu.views import all_data

urlpatterns = [
    path('all/', all_data),
    
]
