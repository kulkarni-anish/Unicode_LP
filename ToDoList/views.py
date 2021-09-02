
from django.shortcuts import render,redirect

from .models import ToDo
from .forms import ListForm, MyUserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def input_view(request):
    form = ListForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    queryset = ToDo.objects.all()
    context={'form':form,"tasks":queryset}
    return render(request,"list.html",context)

def update_view(request,key):
    obj = ToDo.objects.get(id=key)
    form = ListForm(instance=obj)                   #Renders the form with old data
    up_form = ListForm(request.POST, instance=obj)  #Updates the form with new data
    if up_form.is_valid():
        obj.updates +=1
        up_form.save()
        return redirect('home')
    context = {'form':form,'key':key}
    return render(request,"update.html",context)

def delete_view(request,key):
    obj = ToDo.objects.get(id=key)
    if request.method == 'POST':
        obj.delete()
        return redirect('home')
    context={}
    return render(request,"list.html",context)

def signup_view(request):
    form = MyUserCreationForm               #This renders the empty form
    if request.method=='POST':
        form = MyUserCreationForm(request.POST, request.FILES)      #This adds the POST data to the form
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Sign in successful for ' + user)
            return redirect('login')

    context={'form':form}
    return render(request, 'signup.html',context)

def login_view(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or password is incorrect')

    context={}
    return render(request,'login.html',context)

def logout_view(request):
    logout(request)
    return redirect('login')