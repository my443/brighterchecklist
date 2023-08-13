from django.urls import path
from . import views

urlpatterns = [
    path('checklist/<int:id>', views.checklist, name='checklist'),
    path('checklist/complete/<int:id>', views.complete_item, name='complete'),
    # path('checklist/details/', views.details, name='add'),
    path('checklist/details/<int:id>', views.edit_notes, name='details'),
    path('checklist/details/save/<int:id>', views.save_notes, name='save_notes'),
    path('checklist/assigned/', views.list_assigned_checklists, name='list_assigned_checklists'),

    # path('checklist/<int:id>', views.details, name='detail'),       ## TODO - Decide which pattern is better
    # path('', views.checklist),                                      ## TODO - Remove this. This won't be the default forever.
]