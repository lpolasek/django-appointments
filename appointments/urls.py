from django.conf.urls import patterns, include, url
from appointments import models, forms

urlpatterns = patterns('appointments.views',
   url(r'^$', 'list', {'model': models.Appointment, 'form': forms.Appointment }),
   
   url(r'^appointment/$', 'list', {'model': models.Appointment, 'form': forms.Appointment }, name='appointment'),
   url(r'^appointment/edit/(?P<model_id>\d+)/$', 'edit', {'model': models.Appointment, 'form': forms.Appointment }, name='appointment_edit' ),
   url(r'^appointment/delete/(?P<model_id>\d+)/$', 'delete', {'model': models.Appointment }, name='appointment_delete' ),
   url(r'^appointment/add/$', 'add', {'model': models.Appointment, 'form': forms.Appointment }, name='appointment_add' ), 
   
   url(r'^doctor/$', 'list', {'model': models.Doctor, 'form': forms.Doctor }, name='doctor'),
   url(r'^doctor/appointments/(?P<model_id>\d+)/$', 'appointments_for_doctor', {'model': models.Doctor }, name='appointments_for_doctor' ),
   url(r'^doctor/edit/(?P<model_id>\d+)/$', 'edit', {'model': models.Doctor, 'form': forms.Doctor }, name='doctor_edit' ),
   url(r'^doctor/delete/(?P<model_id>\d+)/$', 'delete', {'model': models.Doctor }, name='doctor_delete' ),
   url(r'^doctor/add/$', 'add', {'model': models.Doctor, 'form': forms.Doctor }, name='doctor_add' ),
)
