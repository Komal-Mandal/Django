from django.shortcuts import render

# Create your views here.
def home(req):
    return render(req,'app1/home.html')

def about(req):
    return render(req,'app1/about.html')
