from django.urls import path
from . import views_customer_signup, views_change_password, views_customer, views_profile

urlpatterns = [
    path('new/', views_customer_signup.new_customer_signup, name='new_customer'),

    path('password/', views_change_password.change_password, name='change_password'),

    path('profile/', views_profile.profile, name='profile'),
    path('list/', views_customer.list_customers, name='list_customers'),

    path('edit/<int:id>', views_customer.edit_customer, name='edit_customer'),
]