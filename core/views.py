from turtle import title
from django.shortcuts import render, HttpResponse

from core.models import Event

# Create your views here.

def get_local_event(request, title_event):
    event = Event.objects.get(title=title_event)
    return HttpResponse('O local do evento é {}'.format(event.local))
