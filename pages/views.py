
from unittest import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from .forms import visitorform
from .models import visitor
from django.urls import reverse




def base1(request):
    return render(request,'index.html')

# Create your views here.
def visitorview(request):
    if request.method=='POST':
    #     # a=visitor()
    #     form=visitorform(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('visitorview')
        name=request.GET.get('name')
        location=request.GET.get('location')
        phone=request.GET.get('phone')
        disability=request.GET.get('disability')
        context={
            'name':name,
            'location':location,
            'phone':phone,
            'disability':disability
        }
        template=loader.get_template('index.html')
        return render(template)
            
    else:
        form=visitorform()
        return render(request,'index.html',{'form':form})




    