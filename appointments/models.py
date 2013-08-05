from django.db import models
from django.db.models import Q
from django.core import exceptions

class Doctor(models.Model):
	name = models.CharField(max_length=60)

	def __unicode__(self):
		return self.name

class Appointment(models.Model):
	patient_name = models.CharField(max_length=60)
	time = models.DateTimeField()
	doctor = models.ForeignKey(Doctor)

	def __unicode__(self):
		return ("%s at %s with %s.") % (self.patient_name, self.time, self.doctor.name)

	
	#def clean(self, *args, **kwargs):
		#reject_id=self.id
		#if Appointment.objects.filter(~Q(id=reject_id), time=self.time,doctor=self.doctor):
			#raise exceptions.ValidationError("Doctor is busy!!")
		#super(Appointment,self).clean(*args, **kwargs)

	class Meta:
		ordering = [ 'time' ]
