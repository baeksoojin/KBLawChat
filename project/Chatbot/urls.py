from django.urls import path, include

from . import views

app_name='Chatbot'

urlpatterns = [
    path('', views.home, name="home"),
    path('chatanswer', views.chatanswer, name="chatanswer"),
]