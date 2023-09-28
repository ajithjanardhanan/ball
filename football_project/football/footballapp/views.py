from django.http import HttpResponse
from django.shortcuts import render
from .models import place

# Create your views here.
def demo(request):
    contact = place.objects.all()
    return render(request,"about.html",{'imag':contact})

#def about(request):
    #return render(request,"about.html")