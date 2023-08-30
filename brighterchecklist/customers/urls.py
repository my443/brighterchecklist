from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.new_customer_signup, name='new_customer'),
]