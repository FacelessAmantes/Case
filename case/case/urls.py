from django.contrib import admin
from django.urls import path
from hello import views
from django.views.generic import TemplateView

urlpatterns = [
    path("authorisation/", TemplateView.as_view(template_name ='authorisation.html')),
    path("registration/", TemplateView.as_view(template_name ='registration.html'))
]