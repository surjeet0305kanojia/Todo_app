from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.contrib.auth import authenticate,login as login_user ,logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from application.forms import Todoform
from application.models import Todo
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='login')
def home(request):
    if request.user.is_authenticated:
        user=request.user
        form=Todoform()
        todos=Todo.objects.filter(user=user).order_by('priority')
        return render(request,'index.html',context={'form':form,'todos':todos})
# login functionality
def login(request):
    if request.method =="GET":
        form=AuthenticationForm()
        context={
        "form":form
    }
        return render(request,'login.html',context=context)
    else:
        form=AuthenticationForm(data=request.POST)
        print(form.is_valid)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user =authenticate(username=username ,password=password)
            if user is not None:
                login_user(request,user)
                return redirect('home')
        else:
            context={
        "form":form
        }
            return render(request,'login.html',context=context)



# sign up functionality of app
def signup(request ):
    if request.method == 'GET':
        form=UserCreationForm()
        context={
        "form":form
        }
        return render(request,'signup.html',context=context)
    else:
        print(request.POST)
        form=UserCreationForm(request.POST)
        context={
        "form":form
        }
        if form.is_valid():
            user=form.save()
            print(user)
            if user is not None:
                return redirect('login')
        else:
             return render(request,'signup.html',context=context)
        
@login_required(login_url='login')    
def add_todo(request):
    if request.user.is_authenticated:
        user=request.user
        form=Todoform(request.POST)
        if form.is_valid():
            todo=form.save(commit=False)
            todo.user=user
            todo.save()
            return redirect('home')
        else:
            return render(request,'index.html',context={'form':form})

# delete-todo functionality
def delete_todo(request,id):
    Todo.objects.get(pk=id).delete()
    return redirect('home')



def change_todo(request,id,status):
    todo=Todo.objects.get(pk=id)
    todo.status=status
    todo.save()
    return redirect('home')

# signout functionality
def signout(request):
    logout(request)
    return redirect('login')





