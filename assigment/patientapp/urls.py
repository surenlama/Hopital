from django.contrib import admin
from django.urls import path
from .views import PatientCreate,AppointmentCreate,PatientList,PatientUpdate,PatientDelete,AppointmentList



urlpatterns = [
    path('patient/create/', PatientCreate.as_view(), name="patient-create"),
    path('patient/list/', PatientList.as_view(), name="patient-list"),
    path('patient/update/<str:pk>/', PatientUpdate.as_view(), name="patient-update"),
    path('patient/delete/<str:pk>/', PatientDelete.as_view(), name="patient-delete"),

    path('appointment/create/', AppointmentCreate.as_view(), name="appointment-create"),
    path('appointment/list/', AppointmentList.as_view(), name="appointment-list"),


]
