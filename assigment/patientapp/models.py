
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Patient(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    profile_pic= models.ImageField(upload_to='media',null=True,blank=True)
    address = models.CharField(max_length=40)
    phoneNumber = models.CharField(max_length=20,null=False)
    symptoms = models.CharField(max_length=100,null=False)
    admitDate=models.DateField(null=True)

    def __str__(self):
        return self.first_name

class Appointment(models.Model):
    patientName = models.ForeignKey(Patient,on_delete=models.CASCADE,related_name="patient",null=True)
    doctorName = models.ForeignKey(User,on_delete=models.CASCADE)
    appointmentDate = models.DateField()
    appointmentTime = models.TimeField()
    description = models.TextField(max_length=500)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.patientName.first_name