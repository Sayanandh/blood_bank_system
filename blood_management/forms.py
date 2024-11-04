from django import forms
from .models import Donor, BloodInventory, Hospital

class DonorForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = ['full_name', 'email', 'phone', 'blood_type']

class BloodInventoryForm(forms.ModelForm):
    class Meta:
        model = BloodInventory
        fields = ['blood_type', 'quantity']

class HospitalForm(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = ['hospital_id', 'password' , 'name']
