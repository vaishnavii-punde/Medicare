from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_reminder, name='add_reminder'),
    path('view/', views.view_reminders, name='view_reminders'),
    path('edit/<int:reminder_id>/', views.edit_reminder, name='edit_reminder'),
    path('delete/<int:reminder_id>/', views.delete_reminder, name='delete_reminder'),
]
