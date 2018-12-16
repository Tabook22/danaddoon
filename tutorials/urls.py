from django.urls import path, include
from . import views

urlpatterns = [
path('', views.tutorials, name='tutorials'),
path('<int:tutorial_id>', views.tutorial, name='tutorial'),
path('search', views.search, name='search'),
]