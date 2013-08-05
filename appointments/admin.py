from django.contrib import admin
from appointments.models import *

#class AuthorAdmin(admin.ModelAdmin):
#	list_display = ('first_name', 'last_name', 'email')
#	search_fields = ('first_name', 'last_name')
#
#class BookAdmin(admin.ModelAdmin):
#	list_display = ('title', 'publishers', 'publication_date')
#	list_filter = ('publication_date',)
#	date_hierarchy = 'publication_date'
#	ordering = ('-publication_date',)
#	filter_horizontal = ( 'authors', )
#	raw_id_fields = ( 'publishers', )

admin.site.register(Doctor)
admin.site.register(Appointment)

