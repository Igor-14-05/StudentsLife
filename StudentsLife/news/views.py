from django.shortcuts import render #с помощью него можем указывать какой кусочек html должен отобразиться
from django.http import HttpResponse
from django.views.generic import DetailView

def index(request):
    return render(request, 'news/index.html')


