from django.contrib import admin
from .models import Flight, Airport, Passenger


#if we wish to see all aspects of a flight in the admin interface
class FlightAdmin(admin.ModelAdmin):
    list_display = ("id", "origin", "destination", "duration")

#learn lefthorizontal

		


# Register your models here.
admin.site.register(Flight, FlightAdmin)
admin.site.register(Airport)
admin.site.register(Passenger)



