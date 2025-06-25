from django import forms
from .models import MedicineReminder
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ReminderForm(forms.ModelForm):
    class Meta:
        model = MedicineReminder
        fields = '__all__'
        widgets = {
            'dosage_time': forms.TimeInput(attrs={'type': 'time'}),
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

class SymptomForm(forms.Form):
    symptoms = forms.CharField(
        label='Enter your symptoms',
        widget=forms.TextInput(attrs={'placeholder': 'e.g., fever, cough'}),
        max_length=255
    )

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
