from django.shortcuts import render
from student.forms import Registration

# Create your views here.
def registration(req):
    fm = Registration(field_order=["roll",'city'])
    return render(req,'student/registration.html',{"form":fm})