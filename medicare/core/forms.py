from django import forms
from .models import MedicineReminder

class ReminderForm(forms.ModelForm):
    class Meta:
        model = MedicineReminder
        fields = '__all__'
        widgets = {
            'dosage_time': forms.TimeInput(attrs={'type': 'time'}),
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }
