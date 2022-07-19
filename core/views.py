from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def render_index(request):
    return render(request, 'index.html')

def render_nothing(request):
    return redirect('/index/')

def render_login(request):
    return render(request, 'login.html')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)

        if usuario is not None:
            login(request, usuario)
            return redirect('/index')
        else:
            return redirect('/index')
    else:
        return redirect('/index')

def submit_logout(request):
    logout(request)
    return redirect('/logout_successful/')

def render_logout(request):
    return render(request, 'logout_successful.html')