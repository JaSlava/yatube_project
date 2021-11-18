# posts/views.py
from django.http import HttpResponse
from django.shortcuts import render

# Главная страница
def index(request):    
    return HttpResponse('Главная страница')

def group_posts(request, slug):    
    return HttpResponse('Будущие поcты, отфильтрованные по группам')