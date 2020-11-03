from django.urls import path
from django.conf.urls import include, url
from django.conf.urls.static import static
from dictionary_project import settings
from dictionary.views import dict_home, word, word_mean

urlpatterns = [
    url('dict_home/$', dict_home),
    url('word/$', word),
    url('dict_home/$', dict_home),
    path('word_mean/<words>/', word_mean),
]