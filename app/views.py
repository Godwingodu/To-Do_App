from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .forms import *
from django.contrib.auth.decorators import login_required


# Create your views here.
def Home(request):
    auth.logout(request)
    return render(request,'index.html')


def Signup(request):
    if request.method == 'GET':      
        return render(request,'signup.html')
    else:
        user_name=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']
        if password1==password2:
            if User.objects.filter(username=user_name).exists():
                messages.info(request,'username taken')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect('signup')
            else:
                user=User.objects.create_user(username=user_name,password=password1,email=email)
                user.save()
                messages.success(request,"Todo added succesfully")
                return redirect ('login')
        else:
            messages.info(request,'password not matching')
            return redirect('signup')

def Login(request):
    auth.logout(request)
    if request.method=='GET':
        return render(request,'login.html')
    else:
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user:
            auth.login(request,user)
            return redirect('viewtodo')
        else:
            messages.warning(request,'Invalid credentials')
            return redirect('login')

def Logout(request):
    auth.logout(request)
    return redirect('/')

@login_required(login_url='login')
def ViewTodo(request):
    if request.method == 'GET': 
        if request.user.is_authenticated:
            user=request.user
            todo=Todo.objects.filter(user=user).order_by('priority')
            return render(request,'viewtodo.html',{'todo':todo})
        else:
            return render(request,'login.html')


        
@login_required(login_url='login')
def AddTodo(request):
    if request.method == 'GET': 
        if request.user.is_authenticated:
            form=TodoForm()
            return render(request,'addtodo.html',{'form':form})
        else:
            return render(request,'login.html')
    else:
        if request.user.is_authenticated:
            user=request.user
            form=TodoForm(request.POST)
            if form.is_valid():
                todo=form.save(commit=False)
                todo.user=user
                todo.save()
                messages.success(request,"Account created succesfully")
                return redirect('viewtodo')
            else:
                return render(request,{'form':form})
            
@login_required(login_url='login')            
def DeleteTodo(request,id):
    Todo.objects.filter(id = id).delete()
    return redirect('viewtodo')


@login_required(login_url='login')
def EditTodo(request,id):
    if request.method == 'GET': 
        if request.user.is_authenticated:
            forms=Todo.objects.get(id = id)
            form=TodoForm(instance=forms)
            return render(request,'edittodo.html',{'form':form})
        else:
            return render(request,'login.html')
    else:
        if request.user.is_authenticated:
            user=request.user
            forms=Todo.objects.get(id = id)
            form=TodoForm(instance=forms,data=request.POST)
            if form.is_valid():    
                form.instance.user=user
                form.save()
                #!-- another method--!
                # todo=Todo.objects.get(id = id)
                # todo.user=user
                # todo.title=form.cleaned_data.get('title')
                # todo.status=form.cleaned_data.get('status')
                # todo.priority=form.cleaned_data.get('priority')
                # todo.save()
                #!-- another method--!
                return redirect('viewtodo')
            else:
                return render(request,'EditTodo.html',{'form':form})
            
@login_required(login_url='login')            
def search(request): 
    if request.method == 'GET': # this will be GET now      
        searchinput =  request.GET.get('search') or '' # do some research what it does       
        if searchinput:
           
            todo = Todo.objects.filter(title__icontains=searchinput,user=request.user) # filter returns a list so you might consider skip except part
            return render(request,"viewtodo.html",{"searchinput":searchinput,'todo':todo})
        else:
            todo = Todo.objects.filter(user=request.user).order_by('priority')
            return render(request,"viewtodo.html",{"searchinput":searchinput,'todo':todo})
