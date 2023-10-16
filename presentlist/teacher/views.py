from django.shortcuts import render
from teacher.models import present


# Create your views here.

def addteacher(request):
    p=present.objects.all()
    return render(request,'teachertable.html',{'a':p})

# def viewteacher(request):
#     ass=assighn.objects.all()
#     return render(request,'teachertable.html',{'a':ass})



