from django.contrib import admin
from patientapp.models import Patient,Appointment
# Register your models here.
admin.site.register(Patient)
admin.site.register(Appointment)
