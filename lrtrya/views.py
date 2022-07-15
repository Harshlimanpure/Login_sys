from django.shortcuts import render ,redirect 
from .forms import *
from .models import * 
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method =='POST':
        form = RegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterationForm()
    return render(request, 'register.html',{'form':form})
    