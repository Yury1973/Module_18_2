from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class Index(TemplateView):
    template_name = 'class.html'


def index2(request):
    return render(request, 'function.html')
