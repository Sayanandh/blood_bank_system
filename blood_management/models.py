from django.db import models

class Donor(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)  # Ensure emails are unique
    phone = models.CharField(max_length=15)
    blood_type = models.CharField(max_length=3)

    def __str__(self):
        return self.full_name

class BloodInventory(models.Model):
    blood_type = models.CharField(max_length=3)
    quantity = models.PositiveIntegerField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.blood_type} - {self.quantity} units"

class Hospital(models.Model):
    hospital_id = models.AutoField(primary_key=True)  # AutoField if you want it to auto-increment
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)  # Or any other fields you need

    def __str__(self):
        return self.name
