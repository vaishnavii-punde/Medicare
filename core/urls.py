from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home (can have welcome/dashboard)
    
    # Auth-related paths
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    
    # Medicine suggestion (login required)
    path('suggest/', views.suggest_medicine, name='suggest'),

    # Reminder routes (login required)
    path('reminder/add/', views.add_reminder, name='add_reminder'),
    path('reminder/view/', views.view_reminders, name='view_reminders'),
    path('reminder/edit/<int:reminder_id>/', views.edit_reminder, name='edit_reminder'),
    path('reminder/delete/<int:reminder_id>/', views.delete_reminder, name='delete_reminder'),

    # Email test
    path('test-email/', views.test_email, name='test_email'),
]
