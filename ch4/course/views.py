from django.shortcuts import render

def hello(req):
    return render(req,'course/django.html')
