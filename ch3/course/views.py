from django.shortcuts import render
from datetime import datetime


#def hello(request):
  #  name = "komal"
   # duration = '4 months'
   # seats = 12
    #course_details = {"nm":name,"du":duration,"sea":seats}
    #return render(request,'course/django.html',course_details)

# filters
# def hello(request):
      
   
    # return render(request,'course/django.html',context={"name":"komal","desc":"django is the user friendly language"})

# date and time
#def hello(request):
    #d = datetime.now()
    #return render(request,'course/django.html',context={"dt":d})

# float format
#def hello(request):
   
   # return render(request,'course/django.html',context= {"p1":45.5678,"p2":5.0000,"p3":56.567})

# if tag
#def hello(request):
       
 #return render(request,'course/django.html',context= {"nm":"komal","st":10})

# if tag
def hello(request):
    student = {"names":["raj","anu","riya"]}
    return render(request,'course/django.html',context=student)


def hello(request):
    student = {
        "stu1":{"name":"aa","roll no":1},
        "stu2":{"name":"bb","roll no":2},
        "stu3":{"name":"cc","roll no":3}
    }
    stu = {"stu":student}         
    return render(request,'course/django.html',context=stu)
