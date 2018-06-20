from django.views.generic import ListView, DetailView
from django.views.generic import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from . import models

class CourseListView(ListView):
    model = models.Course
    template_name = 'courses_list.html'