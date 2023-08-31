from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.new_customer_signup, name='new_customer'),
    path('save/', views.save_customer_sign_up, name='save_customer'),
    path('thankyou/', views.thankyou, name='thank_you'),
]