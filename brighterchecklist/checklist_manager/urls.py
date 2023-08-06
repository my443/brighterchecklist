from django.urls import path
from . import views

urlpatterns = [
    path('manager/', views.manager, name='manager'),
    path('manager/new/', views.new, name='new'),
    path('manager/delete/<int:id>', views.delete, name='delete'),
    path('manager/edit/<int:id>', views.edit, name='edit'),
    path('manager/save/<int:id>', views.save, name='save'),

    path('manager/template/list/<int:checklist_id>', views.list_template_items, name='template'),
    path('manager/template/edit/<int:item_id>', views.edit_template_item, name='edit_template_item'),
    path('manager/template/save/<int:item_id>', views.save_template_item, name='save_template_item'),
    path('manager/template/new/<int:checklist_id>', views.new_template_item, name='new_template_item'),
    path('manager/template/delete/<int:item_id>', views.delete_template_item, name='delete_template_item'),
]