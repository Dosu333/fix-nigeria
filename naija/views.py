from django.shortcuts import render

from django.views.generic import TemplateView
from .models import *

class HomePage(TemplateView):
    template_name = 'index.html'

    def get(self,request):
        problems = Problem.objects.all()
        template_data = {'problems':problems}
        
        return render(request, self.template_name, template_data)

class SolutionView(TemplateView):
    template_name = 'list-solution.html'

    def get(self,request,pk):
        solutions = Solution.objects.filter(problem__id=pk)
        template_data = {'solutions':solutions}

        return render(request, self.template_name, template_data)