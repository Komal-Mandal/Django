
from django.urls import path
from app2.views import learn_django,learn_python

urlpatterns = [
    path('django/',learn_django,name='django'),
    path('python/',learn_python,name='python'),
    
]
