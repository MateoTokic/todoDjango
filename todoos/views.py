from django.shortcuts import render, redirect
from django.http import HttpResponse
from todoos.models import Task


def addTask(request):
    task = request.POST.get('task', '')
    Task.objects.create(task=task)
    return redirect('home')

