from django.urls import path
from . import views

urlpatterns = [
    path('manager/', views.manager, name='manager'),
    path('manager/new/', views.new, name='new')
]