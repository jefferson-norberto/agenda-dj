from turtle import title
from urllib import response
from django.shortcuts import render, HttpResponse, redirect
from core.models import Event

# Create your views here.

def get_local_event(request, title_event):
    event = Event.objects.get(title=title_event)
    return HttpResponse('O local do evento é {}'.format(event.local))

def list_events(request):
    event = Event.objects.all()
    data = {'eventos': event}
    return render(request, 'agenda.html', data)

def index(request):
    return redirect('/agenda/')
