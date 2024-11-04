from django.urls import path
from .views import home, register_donor, blood_inventory, add_blood_inventory, hospital_login, hospital_dashboard, contact

urlpatterns = [
    path('', home, name='home'),
    path('register_donor/', register_donor, name='register_donor'),
    path('blood_inventory/', blood_inventory, name='blood_inventory'),
    path('add_blood_inventory/', add_blood_inventory, name='add_blood_inventory'),
    path('hospital_login/', hospital_login, name='hospital_login'),
    path('hospital_dashboard/', hospital_dashboard, name='hospital_dashboard'),
    path('contact/', contact, name='contact'),
]
