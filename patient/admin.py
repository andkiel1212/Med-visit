from django.contrib import admin
from .models import Patient, Visit

# Register your models here.


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = (
        "name_patient",
        "surname_patient",
        "phone_number",
        "email",
    )


@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = ("patient", "date_visit")
