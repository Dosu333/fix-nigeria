from django.urls import path
from .views import *

app_name = 'naija'

urlpatterns = [
    path('list-solution/<int:pk>/', SolutionView.as_view(), name='list-solution'),
    path('create/', CreateSolutionView.as_view(),name='create'),
    path('vote/<int:pk>/', vote_solution_view, name='vote'),
    path('create-profile/<int:pk>/',ProfileCreateView.as_view(),name='create-profile'),
]