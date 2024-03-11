from django.urls import path, include
from . import views
#include - чтобы начать отслеживать переходы на приложения и чтобы уже дальше все отслеживалло приложение
#здесь по сути отсулеживаем различные url адреса
#можно прописывать что какие приложения должны открывать при той или иной ссылке
urlpatterns = [
    path('',views.index), #при обращении к главной страничке сработать должен метод views
    path('about/',views.about),
    # path("univeristy/", include('university.urls',  namespace='univeristy'), name="university-info"),
    # path("news/", include('news.urls',  namespace='news'), name="news"),
    path('news/<int:pk>', views.newsdetail.as_view(), name="news-detail")
]
