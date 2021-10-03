from django.db import models

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