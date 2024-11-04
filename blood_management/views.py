from django.shortcuts import render, redirect
from .models import Donor, BloodInventory, Hospital
from .forms import DonorForm, BloodInventoryForm
from django.contrib import messages
from django.contrib.auth import login

# Render the home page
def home(request):
    return render(request, 'index.html')

def register_donor(request):
    if request.method == 'POST':
        form = DonorForm(request.POST)
        if form.is_valid():
            # Check for duplicate email
            if Donor.objects.filter(email=form.cleaned_data['email']).exists():
                messages.error(request, "A donor with this email already exists.")
                return redirect('register_donor')
            
            # Save the donor
            donor = form.save()

            # Update blood inventory
            blood_type = donor.blood_type  
            inventory, created = BloodInventory.objects.get_or_create(blood_type=blood_type)
            inventory.quantity += 1 
            inventory.save()

            messages.success(request, "Thank you for registering! Your information has been saved.")
            return redirect('home')  # Redirect to the home page
    else:
        form = DonorForm()

    return render(request, 'register.html', {'form': form})

def add_blood_inventory(request):
    if request.method == 'POST':
        form = BloodInventoryForm(request.POST)
        if form.is_valid():
            # Get blood type and quantity
            blood_type = form.cleaned_data['blood_type']
            quantity = form.cleaned_data['quantity']
            expiration_date = form.cleaned_data['expiration_date']

            # Update or create the inventory entry
            inventory, created = BloodInventory.objects.get_or_create(blood_type=blood_type)
            inventory.quantity += quantity
            inventory.expiration_date = expiration_date
            inventory.save()

            messages.success(request, "Blood inventory has been updated.")
            return redirect('blood_inventory')  # Redirect to the blood inventory page
    else:
        form = BloodInventoryForm()

    return render(request, 'add_blood_inventory.html', {'form': form})

def blood_inventory(request):
    inventories = BloodInventory.objects.all()
    return render(request, 'inventory.html', {'inventories': inventories})

def hospital_login(request):
    if request.method == 'POST':
        hospital_id = request.POST.get('hospital_id')
        password = request.POST.get('password')

        print(f'Trying to authenticate Hospital ID: {hospital_id} with Password: {password}')  # Debugging line

        # Attempt to authenticate the hospital
        hospital = authenticate_hospital(hospital_id, password)

        if hospital:
            # If authentication is successful, log in and redirect
            login(request, hospital)
            return redirect('hospital_dashboard')  # Redirect to hospital dashboard
        else:
            messages.error(request, 'Invalid Hospital ID or Password.')

    return render(request, 'login.html')


def hospital_dashboard(request):
    return render(request, 'hospital_dashboard.html')

def authenticate_hospital(hospital_id, password):
    try:
        # Fetch the hospital based on hospital_id
        hospital = Hospital.objects.get(hospital_id=hospital_id)  # Correct field used
        
        # Compare plain text passwords
        if hospital.password == password:  
            return hospital
        else:
            return None
    except Hospital.DoesNotExist:
        return None


def contact(request):
    return render(request, 'contact.html')
