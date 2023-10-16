from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

#create your viewss here
def attendence_sheet(request):
    return render(request,'attendancesheet.html')

def log_in(request):
    if request.method=='post':
        name=request.post['name']
        password=request.post['password']

        user=authenticate(name=name,password=password)

        if user is not None:
            login(request,user)
            return HttpResponse('login')
        else:
            return redirect('signup')

    return render(request,'login.html')


def sign_up(request):
    if request.method =='post':
        name=request.post['name']
        email=request.post['email']
        password=request.post['password']

        myuser=User.object.create_user(name,email,password)
        myuser.save()
        return redirect('login')
    return render(request,'signup.html')
