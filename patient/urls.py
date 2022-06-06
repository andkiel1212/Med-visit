from django.urls import path
from . import views


urlpatterns = [
    path("", views.patient_list, name="patient-list"),
    path("<str:patient_id>/", views.patient_detail, name="patient-detail"),
    path("<str:patient_id>/<str:visit_id>", views.visit_detail, name="visit-detail"),
    path("htmx/search-patients/", views.search_patients, name="search-patients"),
    path("create-patient/", views.create_patient, name="create-patient"),
    path("calendar/", views.calendar, name="calendar"),
]
