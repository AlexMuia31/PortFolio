from django.shortcuts import render

from django.views.generic import ListView ,DetailView

from .models import Job

class home(ListView):
    queryset = Job.objects.all()
    template_name='jobs/home.html'

