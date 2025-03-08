from django.shortcuts import render
from stu.models import profile

# Create your views here.
def all_data(req):
    stu = profile.objects.all()
    print(stu)
    return render(req,'stu/all.html',{"stu":stu})