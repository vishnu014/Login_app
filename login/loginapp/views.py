from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse



        

def indexview(request):
    return render(request,'login.html')



def loginview(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('dashboard'))
        else:
            return HttpResponse('Please enter valid details.')
        
    return render(request, 'login.html')

def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard.html')
    else:
        return redirect(reverse('login'))
