from django import forms
from appointments import models

class Doctor(forms.ModelForm):
	class Meta:
		model = models.Doctor

class Appointment(forms.ModelForm):

	class Meta:
		model = models.Appointment
		widgets = { 'time': forms.DateTimeInput(format='%Y-%m-%d %H:%M') }
