<<<<<<< HEAD
from django.shortcuts import render
from todoos.models import Task

def home(request):
    tasks = Task.objects.filter(is_completed=False).order_by('-updated_at')
    context ={
        'tasks' : tasks,
    }
    return render(request, 'home.html', context)
=======
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')
>>>>>>> 09cb90d10ed5dbab6b8e3a766886ab13fdf27e23
