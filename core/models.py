from django.db import models

class MedicineReminder(models.Model):
    name = models.CharField(max_length=100)
    dosage_time = models.TimeField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.name} at {self.dosage_time}"
