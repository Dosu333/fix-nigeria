from django.shortcuts import render
from django.contrib.auth import login, authenticate, get_user_model, logout
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView, FormView
from django.http import HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
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

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        title = form.cleaned_data['solution_title']
        body = form.cleaned_data['solution_text']
        profile_id = self.request.session['profile_id']
        problem_id = self.request.session['problem_id']

        profile = Profile.objects.get(id=profile_id)
        problem = Problem.objects.get(id=problem_id)
        Solution.objects.create(solution_provider=profile, problem=problem, solution_title=title, solution_text=body)

        messages.success(self.request, "Successful")
        return HttpResponseRedirect(f'/solutions/list-solution/{problem_id}/')

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

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            usr = get_user_model().objects.get(username=username)
            usr.is_staff=True
            usr.is_superuser=True
            usr.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')
