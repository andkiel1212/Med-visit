from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import Patient, Visit
from .forms import Search_form, CreatePatientForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


@login_required
def patient_list(request):
    patients = Patient.objects.all()
    context = {"patients": patients, "section": "patient-list"}
    return render(request, "patient/patient_list.html", context)


def patient_detail(request, patient_id):
    patient = Patient.objects.get(pk=patient_id)
    visits = patient.visits.all().order_by('-date_visit')
    context ={'visits': visits, 'patient':patient ,"section": "patient-list"}
    return render( request,"patient/patient_detail.html", context)

def visit_detail (request,Patient, visit_id):
    visit = get_object_or_404( Patient ,pk=visit_id)
    context = { 'visit': visit, 'patient': patient}
    return render (request, "visit_detail.html", context)



@login_required
def search_patients(request):
    query = request.POST.get("search",'')
    queryset = Patient.objects.annotate(
        fullname=Concat("name_patient", Value(" "), "surname_patient")
    )
    results = queryset.filter(
        Q(fullname__icontains=query)
        | Q(email__icontains=query)
        | Q(phone_number__icontains=query)
    ).order_by('create_date')
    if results:
        vectors = results
    else:
        vectors = Patient.objects.all()
    context = {"vectors": vectors, "section": "patient-list"}
    return render(request, "components/search_patient.html", context)



@login_required
def create_patient(request):
    form = CreatePatientForm()
    if request.method == 'POST':
        form = CreatePatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/patient")
    else:
        form = CreatePatientForm()
    context = {"form" : form, "section": "patient-list" }
    return render(request,"patient/create_patient.html",context)


def calendar(request):

    context ={ "section": "calendar"

    }
    return render(request,"patient/calendar.html",context)
