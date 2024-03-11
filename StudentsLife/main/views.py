from django.shortcuts import render #с помощью него можем указывать какой кусочек html должен отобразиться
from django.http import HttpResponse
from .models import Articles
from django.views.generic import DetailView
# Create your views here.

def index(request):
    return render(request, 'main/index.html')

def about(request):
    news = Articles.objects.order_by("-date")
    return render(request, 'main/about.html', {"news" : news})
    # return HttpResponse(f"<h4>{request}</h4>")

class newsdetail(DetailView):
    model = Articles
    template_name = 'news/detail.html'
    context_object_name = 'article'

