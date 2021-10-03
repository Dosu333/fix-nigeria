from django.shortcuts import render

from django.views.generic import TemplateView, FormView
from django.urls import reverse
from django.shortcuts import redirect
from .models import *
from .forms import *

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

class CreateSolutionView(FormView):
    template_name = 'create-solution.html'
    form_class = SolutionForm
    

class ProfileCreateView(FormView):
    template_name = 'profile_form.html'
    form_class = ProfileForm

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        name = form.cleaned_data['fullname']
        email = form.cleaned_data['contact_email']
        acc_number = form.cleaned_data['account_number']
        bank = form.cleaned_data['bank']
        acct_name = form.cleaned_data['account_name']

        profile, created = Profile.objects.get_or_create(fullname=name,contact_email=email,account_number=acc_number,bank=bank,account_name=acct_name)
        self.request.session['profile_id'] = profile.id
        self.request.session['problem_id'] = self.kwargs['pk']
        return redirect('naija:create')
        # return super().form_valid(form)
