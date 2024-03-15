from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_first_model, name='add_first_model'),
    path('list/', views.list_first_models, name='list_first_models'),
]
