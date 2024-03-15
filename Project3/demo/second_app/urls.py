from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_second_model, name='add_second_model'),
    path('list/', views.list_second_models, name='list_second_models'),
]
