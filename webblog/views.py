from django.shortcuts import render,redirect
import requests
import random
from . models import Usersinfo
from .forms import ImageForm
import json
from django.urls import reverse
from . models import Blogs
def login(request):
    UserNotExist=False
    if request.method=='POST':
        Username=request.POST['username']
        Password=request.POST['password']
        if Usersinfo.objects.filter(username=Username,password=Password).values("username","password").count()==1:
            print("jbksdkadfjhhfbaksjhfkjhfshfkhs")
            return redirect('Dashboard',username=Username)
        else:
            UserNotExist=True

    return render(request,'login.html',{'UserNotExists':UserNotExist})

            
        


def register(request):
    UserAlreadyExist=False
    PasswordNotMatch=False
    ShortPassword=False
    CaptchaNotVerify=False
    AddNotVerify=False
    VerifyNoOne=random.randint(0,500)
    VerifyNoTwo=random.randint(30,600)
    if request.method == 'POST':
        Username=request.POST['username']
        Password=request.POST['password']
        ConfirmPassword=request.POST['ConfirmPassword']
        
        # Google recaptcha
        # clientKey=request.POST['g-recaptcha-response']
        # secretKey="6LeqVWcaAAAAAB9GzRUDDJiRgMdsIx_UYJhOyHcp"

        # captcha={
        #     'secret':secretKey,
        #     'response':clientKey
        # }

        # res=requests.post("https://www.google.com/recaptcha/api/siteverify",data=captcha)
        # response=json.loads(res.text)
        # verified=response['success']

        if(int(request.POST['Verification'])!=int(request.POST['sum'])):
            AddNotVerify=True

        
        if(not(AddNotVerify)):
            if(Password==ConfirmPassword):
                if(len(Password)>8):
                    if Usersinfo.objects.filter(username=Username).values("username").count()==0:
                        user=Usersinfo(username=Username,password=Password)
                        user.save()
                    else:
                        UserAlreadyExist=True
                else:
                    ShortPassword=True
            else:
                PasswordNotMatch=True
    

            
    return render(request,'register.html',{'UserAlreadyExist':UserAlreadyExist,'PasswordNotMatch':PasswordNotMatch,'ShortPassword':ShortPassword,'CaptchaNotVerify':CaptchaNotVerify,'VerifynoOne':VerifyNoOne,'VerifynoTwo':VerifyNoTwo,'AddNotVerify':AddNotVerify,'sum':VerifyNoOne+VerifyNoTwo})

def Dashboard(request,username):
    UserNotFound=False
    YouDontHaveBlogs=False
    if  request.method=='POST':
        if 'search' in request.POST:
            user=request.POST['user']
            if Usersinfo.objects.filter(username=user).count()==0:
                UserNotFound=True
            if Usersinfo.objects.filter(username=user).count()==1:
                return redirect('userspage',username=user)
        if 'createblog' in request.POST:
            return redirect('AddArticle',username=username)
        if 'logout' in request.POST:
            return redirect('login')

        
    
        

    blogs=Blogs.objects.filter(username=username)
    if blogs.count()==0:
        YouDontHaveBlogs=True
    return render(request,'Dashboard.html',{'blogs':blogs,'UserNotFound':UserNotFound,'YouDontHaveBlogs':YouDontHaveBlogs,'user':username})

def userspage(request,username):
    NothingToShow=True
    blogs=Blogs.objects.filter(username=username,privacy=False)
    if blogs.count()!=0:
        NothingToShow=False

    return render(request,'userspage.html',{'NothingToShow':NothingToShow,'blogs':blogs,'user':username})

def AddArticle(request,username):
    if request.method=='POST':
        name=Blogs(username=username)
        form=ImageForm(request.POST,request.FILES,instance=name)
        form.save()
        return redirect('Dashboard',username=username)

    form=ImageForm()

    
    return render(request,'AddArticle.html',{'form':form})