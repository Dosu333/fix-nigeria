from django.urls import path
from .views import *

app_name = 'naija'

urlpatterns = [
    path('list-solution/<int:pk>/', SolutionView.as_view(), name='list-solution'),
]