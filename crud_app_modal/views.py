from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CrudForm
from .models import CrudModel

# Create your views here.
def indexView(request):
    data =  CrudModel.objects.all()
    context = { 'employees': data }   
    return render(request, 'index.html', context)

def createView(request):
    form = CrudForm(request.POST or None)
    if form.is_valid():
        form.save(commit=False)
        form.save()
        messages.add_message(request, messages.SUCCESS, "Employee successfully added")
        return redirect('index')
    
    return redirect('index')      
    # return render(request,'index.html', { 'form': form })

def updateView(request, id):
    data= CrudModel.objects.get(id=id)
    form= CrudForm(request.POST or None, instance=data)
    if form.is_valid():
        form.save(commit=False)
        form.save()
        messages.add_message(request, messages.SUCCESS, "Employee successfully updated")
        return redirect('index')

    context= { 'employees': form }
    return render(request, 'index.html', context)   


def deleteView(request, id):
    data= CrudModel.objects.get(id=id)    
    data.delete()
    messages.add_message(request, messages.SUCCESS, "Employee successfully deleted")
    return redirect('index')