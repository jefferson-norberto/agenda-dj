from django.shortcuts import render, HttpResponse, redirect
from core.models import Event
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from datetime import datetime, timedelta
from django.http.response import Http404, JsonResponse

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

@login_required(login_url='/login/')
def submit_event(request):
    if request.POST:
        title = request.POST.get('title')
        event_date = request.POST.get('event_date')
        description = request.POST.get('description')
        user = request.user
        id_event = request.POST.get('id_event')
        local = request.POST.get('local')
        if id_event:
            event = Event.objects.get(id=id_event)
            if event.user == user:
                event.title = title
                event_date=event_date, 
                event.local=local 
                event.description=description
                event.save()
        else:
            Event.objects.create(title=title, 
                                event_date=event_date, 
                                description=description, 
                                local=local,
                                user=user)
    return redirect('/')

@login_required(login_url='/login/')
def delete_event(request, id_event):
    user = request.user
    try:
        event = Event.objects.get(id=id_event)
    except:
        raise Http404()
    if user == event.user:
        event.delete()
    else:
        raise Http404()
    return redirect('/')
    
def get_local_event(request, title_event):
    event = Event.objects.get(title=title_event)
    return HttpResponse('O local do evento é {}'.format(event.local))

@login_required(login_url='/login/')
def list_events(request):
    user = request.user
    today = datetime.now() - timedelta(hours=1)
    event = Event.objects.filter(user=user, event_date__gt=today)
    data = {'eventos': event}
    return render(request, 'agenda.html', data)

@login_required(login_url='/login/')
def create_event(request):
    id_event = request.GET.get('id')
    datas = {}
    if id_event:
        datas['event'] = Event.objects.get(id=id_event)
    return render(request, 'event.html', datas)

def index(request):
    return redirect('/agenda/')

#Aqui para trabalhar com outro app sem necessidade de login
def json_list_events(request, id_user):
    user = User.objects.get(id=id_user)
    event = Event.objects.filter(user=user).values('id', 'title')
    return JsonResponse(list(event), safe=False)
