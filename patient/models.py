from django.db import models
from django.db.models.enums import Choices
from django.db.models.fields import CharField, DateField
from django.utils import timezone
from django.core.validators import RegexValidator
from django.urls import reverse


class Patient(models.Model):

    name_patient = models.CharField(max_length=100)
    surname_patient = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    
    # comment - unset to testing -

    # phone number to add in to the end
    # phone_regex = RegexValidator(
    #    regex=r"^\?1?\d{9,12}$",
    #    message="Numer telefonu musi mieć format : '*********'.",
    # )
    # phone_number = models.CharField(
    #    validators=[phone_regex], max_length=15, blank=False
    # )  # validators should be a list
    email = models.EmailField(max_length=150, blank=False)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s %s" % (self.name_patient, self.surname_patient)
        
    def get_absolute_url(self):
        return reverse('patient-detail', args=[self.pk])

class Visit(models.Model):

    STATUS_CHOICES = (
        ("yes", "TAK"),
        ("no", "NIE"),
    )

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="visits")
    date_visit = models.DateTimeField(blank=True, null=True)
    description = models.TextField()
    recommendation_visit = models.TextField()
    create_visit = models.DateTimeField(auto_now_add=True)
    execute_visit = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="yes"
    )

    class Meta:
        ordering = ("create_visit",)

    def __str__(self):
        return "Wizyta pacjenta {}".format(self.patient)

    def get_absolute_url(self):
        return reverse('visit-detail', kwargs={'visit_id':self. pk})


class Parent(models.Model):
    patient = models.OneToOneField(
        Patient, on_delete=models.CASCADE, related_name="parent"
    )
    name_parent = models.CharField(max_length=20)
    surname_parent = models.CharField(max_length=20)

    def __str__(self):
        return "%s %s" % (self.name_parent, self.surname_parent)
