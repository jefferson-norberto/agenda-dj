from turtle import title
from urllib import response
from django.shortcuts import render, HttpResponse, redirect
from core.models import Event
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def login_user(request):
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Usuário ou senha invélido')
    return redirect('/')

def get_local_event(request, title_event):
    event = Event.objects.get(title=title_event)
    return HttpResponse('O local do evento é {}'.format(event.local))

@login_required(login_url='/login/')
def list_events(request):
    user = request.user
    event = Event.objects.filter(user=user)
    data = {'eventos': event}
    return render(request, 'agenda.html', data)

def index(request):
    return redirect('/agenda/')
