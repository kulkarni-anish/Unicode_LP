
from django.shortcuts import render,redirect

from .models import ToDo
from .forms import ListForm

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
    form = ListForm(instance=obj)
    up_form = ListForm(request.POST, instance=obj)
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