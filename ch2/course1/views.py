from django.shortcuts import render


# Create your views here.
def course1(request):
    coursename = {"cname":"Django"}
    return render(request,'course1/django.html',context=coursename)
