from django.shortcuts import render

# Create your views here.

def dashboard(request):
    return render(request, 'authentication/dashboard.html')

def home(request):
    return render(request, 'home/index.html')