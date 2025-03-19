from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

def calculate(x, y):
    return x*y

# Create your views here.
def intro(request):
    return render(request, 'base.html' ) 

def about(request):
    return render(request, 'about.html')

def home(request):
    return render(request, 'base.html' ) 

def tools(request):
    return render(request, 'tools_menu.html' ) 

def vo(request):
    return render(request, 'vo.html' ) 

def table(request):
    return render(request, 'table.html' )

def materials(request):
    return render(request, 'materials.html' )

def products(request):
    return render(request, 'products.html' )

def panel(request):
    return render(request, 'panels.html' )

def inverter(request):
    return render(request, 'inverters.html' )

def battery(request):
    return render(request, 'battery.html' )
    
def contact(request):
    return render(request, 'contact.html' ) 

def dev(request):
    return render(request, 'base1.html' )


