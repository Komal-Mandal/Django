
from django.urls import path
from course.views import hello

urlpatterns = [
    path('dj/', hello),
]