from django.http import HttpResponse
from django.shortcuts import render, reverse
import datetime
import os


def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir'),
    }
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_time = datetime.datetime.now().isoformat(timespec='minutes') 
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    # по аналогии с `time_view`, напишите код,
    # который возвращает список файлов в рабочей 
    # директории    
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    listdir = sorted(os.listdir(base_path))
    msg = f'{listdir}'
    return HttpResponse(msg)
