from django.shortcuts import render
from students.models import present1


# Create your views here.
def addstudent(request):
    p=present1.objects.all()
    return render(request,'studenttable.html',{'a':p})