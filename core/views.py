import os
import pickle
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .models import MedicineReminder
from .forms import ReminderForm

# Load model and vectorizer once globally
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model = pickle.load(open(os.path.join(BASE_DIR, 'ml_model', 'med_predictor.pkl'), 'rb'))
vectorizer = pickle.load(open(os.path.join(BASE_DIR, 'ml_model', 'vectorizer.pkl'), 'rb'))


# ========== ML-Based Medicine Suggestion ==========
@login_required
def suggest_medicine(request):
    medicine = None
    if request.method == 'POST':
        symptoms = request.POST.get('symptoms')
        if symptoms:
            X = vectorizer.transform([symptoms])
            medicine = model.predict(X)[0]
    return render(request, 'suggest.html', {'medicine': medicine})


# ========== Reminder Views ==========
@login_required
def add_reminder(request):
    if request.method == 'POST':
        form = ReminderForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'reminder_success.html')
    else:
        form = ReminderForm()
    return render(request, 'add_reminder.html', {'form': form})

@login_required
def view_reminders(request):
    reminders = MedicineReminder.objects.all()
    return render(request, 'view_reminders.html', {'reminders': reminders})

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
    return render(request, 'add_reminder.html', {'form': form})

@login_required
def delete_reminder(request, reminder_id):
    reminder = get_object_or_404(MedicineReminder, id=reminder_id)
    reminder.delete()
    return redirect('view_reminders')


# ========== Dashboard/Home ==========
@login_required
def home(request):
    return render(request, 'home.html')


# ========== Authentication ==========
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')


# ========== Test Email Utility ==========
from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings

def test_email(request):
    send_mail(
        subject='Test Email from Django',
        message='This is a test email to confirm your settings.',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=['workingspace14@gmail.com'],
        fail_silently=False,
    )
    return HttpResponse("Test email sent!")
