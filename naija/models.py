from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Problem(models.Model):
    problem_category = models.ForeignKey(Category,on_delete=models.CASCADE)
    title_of_problem = models.CharField(max_length=150)
    short_description = models.CharField(max_length=255,blank=True,null=True)

    def __str__(self):
        return self.title_of_problem

class Profile(models.Model):
    fullname = models.CharField(max_length=255)
    contact_email  = models.EmailField()
    account_number = models.CharField(max_length=10)
    bank = models.CharField(max_length=255)
    account_name = models.CharField(max_length=255)

    def __str__(self):
        return self.fullname
    
class Solution(models.Model):
    problem = models.ForeignKey(Problem,on_delete=models.CASCADE)
    solution_provider = models.ForeignKey(Profile,on_delete=models.SET_NULL,null=True,blank=True)
    solution_title = models.CharField(max_length=255, blank=True, null=True)
    solution_text = models.TextField()
    user_voted = models.ManyToManyField(get_user_model())

    def __str__(self):
        return self.solution_title