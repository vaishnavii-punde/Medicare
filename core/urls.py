from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('add/', views.add_reminder, name='add_reminder'),
    path('view/', views.view_reminders, name='view_reminders'),
    path('edit/<int:reminder_id>/', views.edit_reminder, name='edit_reminder'),
    path('delete/<int:reminder_id>/', views.delete_reminder, name='delete_reminder'),
    path('suggest/', views.suggest_medicine_view, name='suggest_medicine'),
]
