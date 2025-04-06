from django.contrib import admin
from django.urls import path
from hello import views
from django.views.generic import TemplateView

urlpatterns = [
    path("authorisation/", TemplateView.as_view(template_name ='authorisation.html')),
    path("registration/", TemplateView.as_view(template_name ='registration.html')),
    path("main", TemplateView.as_view(template_name ='main.html')),
    path("resetPass", TemplateView.as_view(template_name ='resetPass.html')),
    path("news", TemplateView.as_view(template_name ='news.html'))
]