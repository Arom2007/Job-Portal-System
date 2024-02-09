from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Category, Job
class HomeView(ListView):
    template_name = 'core/home.html'
    queryset = Job.objects.all()
    context_object_name = 'jobs'
