from django import forms
from .models import Patient,Appointment
from django.contrib.auth import get_user_model

User = get_user_model()
  

#Signupform
class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'profile_pic', 'address', 'phoneNumber', 'symptoms','admitDate']
        #For Label tag
        labels = {  
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'profile_pic': 'Profile Picture',
            'address': 'Address',
            'phoneNumber':'Phone Number',
            'symptoms':'Symptoms',
            'admitDate':'Admitted Date',
        }

    # def clean(self):
    #     cleaned_data = super().clean()
    #     print(cleaned_data)
    #     valpwd = self.cleaned_data['password1']
    #     valrpwd = self.cleaned_data['password2']
    #     if valpwd != valrpwd:
    #         raise forms.ValidationError("Password doesnot match")

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['patientName', 'doctorName', 'appointmentDate', 'appointmentTime', 'description','status']
        #For Label tag
        labels = {  
            'patientName': 'Patient Name',
            'doctorName': 'Doctor Name',
            'appointmentDate': 'Appointment Date',
            'appointmentTime': 'Appointment Time',
            'description':'Description',
            'status':'Status',
        }        
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['doctorName'].queryset=User.objects.filter(user_type="Doctor")


# #login
