from django.shortcuts import render
from django.views.generic import CreateView, ListView
from angel.models import Angel
# Create your views here.


class AngelList(ListView):
    model = Angel
    queryset = Angel.objects.all()
    template_name = 'angel/index.html'
    context_object_name = 'angels'