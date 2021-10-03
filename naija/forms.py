from django.forms import ModelForm
from .models import Profile, Solution

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['fullname','contact_email','account_number','bank','account_name']

class SolutionForm(ModelForm):
    class Meta:
        model = Solution
        fields = ['solution_title','solution_text']