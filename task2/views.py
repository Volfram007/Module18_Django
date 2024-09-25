from django.shortcuts import render
from django.views.generic import TemplateView


def index(request):
    return render(request, 'index.html')


class ClassTemplate(TemplateView):
    template_name = 'second_task/class_template.html'


def func_template(request):
    return render(request, 'second_task/func_template.html')
