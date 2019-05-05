from django.urls import path, re_path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^details/(?P<id>\d+)/$', views.details, name='details'),
]