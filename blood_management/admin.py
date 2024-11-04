from django.contrib import admin
from .models import Donor, BloodInventory, Hospital

admin.site.register(Donor)
admin.site.register(BloodInventory)
admin.site.register(Hospital)
