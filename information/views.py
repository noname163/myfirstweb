import django
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404,redirect
from .models import Tree
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from .forms import CreateUserForm
from django.template import RequestContext
from django.contrib import messages

def login_page(request):
    if request.method =='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user= authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('tree_list_url')
        else:
            messages.info(request,'username or password is incorrect')

    contex={}
    return render(request,'infor/login.html',contex)


def logout_User(request):
    logout(request)
    return redirect('login')

def registration_page(request):
    form = CreateUserForm()
    if request.method =='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Your account have been created ' + user)
            return redirect('infor:login')
    
    registration={'form':form}
    return render(request,'infor/registration.html',registration)

def index(request):
    tree=Tree.objects.all()
    return render(request,'infor/index.html',{'trees':tree})

def detail(request,infor_id):
    tree= get_object_or_404(Tree,pk=infor_id)
    return render(request,'infor/detail.html',{'trees':tree})
