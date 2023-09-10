from django.urls import path
from . import views, views_change_password

urlpatterns = [
    path('new/', views.new_customer_signup, name='new_customer'),
    path('save/', views.save_customer_sign_up, name='save_customer'),
    path('thankyou/', views.thankyou, name='thank_you'),

    path('password/', views_change_password.change_password, name='change_password'),
    path('profile/', views.profile, name='profile'),
]