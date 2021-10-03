from django.shortcuts import render

from django.views.generic import TemplateView
from .models import Problem

class HomePage(TemplateView):
    template_name = 'index.html'

    def get(self,request):
        problems = Problem.objects.all()
        template_data = {'problems':problems}
        
        return render(request, self.template_name, template_data)