from django.shortcuts import render,redirect
from datetime import datetime
from .forms import clientform,NewUserForm,projectForm
from events.models import client,project
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth.models import User, auth

# Create your views here.
def home(request):
    return render(request, 'events/home.html', {})



def all_clients(request):
    form = client.objects.all()
    return render(request,'events/clientlist.html',{'form':form})

def delete(request, id):
    form = client.objects.get(id=id)
    form.delete()
    return redirect('clientlist.html',{'form':form})

def edit(request, id):
    form = client.objects.get(id=id)
    form = clientform(request.POST or None, instance=form)
    if form.is_valid():
        form.save()
        return redirect('listclient') 
    return render(request,"events/edit.html",{'form':form})


 
def registerclient(request):
    form = clientform
    if request.method == 'POST':
       form = clientform(request.POST or None)
       if form.is_valid():
           form.save()
    context ={'form':form} 
    return render(request, "events/registerclient.html", context)

def register_request(request):
     if request.method == 'POST':
         form = NewUserForm(request.POST)
         if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.error(request,"registration sucessfull.")
            return redirect('login')
     else:
         form = NewUserForm()
     context ={'form':form}
     return render(request, "events/register.html", context)


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
            
        form = AuthenticationForm()
    context ={'form':form}
    return render(request, "events/login.html", context)

def project(request):
    form = projectForm
    if request.method == 'POST':
       form = projectForm(request.POST or None)
       if form.is_valid():
        form.save()
    context ={'form':form} 
    return render(request, "events/project.html", context)

def project_list(request):
    form = project.objects.all()
    return render(request,"projectlist.html",{'form':form})
