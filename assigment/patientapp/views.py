from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from patientapp.models import Appointment, Patient
from .forms import PatientForm,AppointmentForm
from .mixins import UserAccessMixins
from assigment.utils import Doctor, Receptionists


# Create your views here.
class PatientCreate(UserAccessMixins,CreateView):
    user_access_type = [Receptionists,]
    form_class = PatientForm
    template_name = "patient.html"
    success_url = '/patient/create/'
    

class PatientList(UserAccessMixins,ListView):
    user_access_type = [Receptionists,]
    model = Patient
    template_name = "patientlist.html"
    success_url = '/patient/list/'
    context_object_name = "patient_list"
    # (muni ko gareni huncha mathi ko gareni huncha)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data()
    #     context['patient_list'] = self.get_queryset()
    #     return context

class PatientUpdate(UserAccessMixins,UpdateView):
    user_access_type = [Receptionists,]
    # queryset = Patient.objects.all()(yo gardani huncha ya model rakhda ni hunhca)
    model = Patient
    form_class = PatientForm
    template_name = "patient.html"
    success_url = '/patient/list/'    


class PatientDelete(UserAccessMixins,DeleteView):
    user_access_type = [Receptionists,]
    # queryset = Patient.objects.all()(yo gardani huncha ya model rakhda ni hunhca)
    model = Patient
    template_name = "patientdelete.html"
    success_url = '/patient/list/'  


class AppointmentCreate(UserAccessMixins,CreateView):
    user_access_type = [Receptionists,]
    form_class = AppointmentForm
    template_name = "appointment.html"
    success_url = '/appointment/create/'


class AppointmentList(UserAccessMixins,ListView):
    user_access_type = [Doctor,]
    model = Appointment
    template_name = "appointmentlist.html"
    success_url = '/appointment/list/'
    context_object_name = "appointment_list"    