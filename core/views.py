from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import MedicineReminder
from .forms import ReminderForm, SymptomForm, RegisterForm
from .ml_model import suggest_medicine

@login_required
def home(request):
    return render(request, 'home.html')

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully.")
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def add_reminder(request):
    if request.method == 'POST':
        form = ReminderForm(request.POST)
        if form.is_valid():
            reminder = form.save(commit=False)
            reminder.save()
            return redirect('view_reminders')
    else:
        form = ReminderForm()
    return render(request, 'add_reminder.html', {'form': form})

@login_required
def view_reminders(request):
    reminders = MedicineReminder.objects.all()
    return render(request, 'view_reminders.html', {'reminders': reminders})

@login_required
def reminder_success(request):
    return render(request, 'reminder_success.html')

@login_required
def suggest_medicine_view(request):
    medicine = None
    if request.method == 'POST':
        form = SymptomForm(request.POST)
        if form.is_valid():
            symptoms = form.cleaned_data['symptoms']
            medicine = suggest_medicine(symptoms)
    else:
        form = SymptomForm()
    return render(request, 'suggest.html', {'form': form, 'medicine': medicine})

@login_required
def edit_reminder(request, reminder_id):
    reminder = get_object_or_404(MedicineReminder, id=reminder_id)
    if request.method == 'POST':
        form = ReminderForm(request.POST, instance=reminder)
        if form.is_valid():
            form.save()
            return redirect('view_reminders')
    else:
        form = ReminderForm(instance=reminder)
    return render(request, 'edit_reminder.html', {'form': form})

@login_required
def delete_reminder(request, reminder_id):
    reminder = get_object_or_404(MedicineReminder, id=reminder_id)
    if request.method == 'POST':
        reminder.delete()
        return redirect()
