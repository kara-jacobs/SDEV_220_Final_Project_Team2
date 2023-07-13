from django.contrib import admin

# references model.py models
from .models import ParkAppUser 
from .models import Venue
from .models import Event

# Register your models here.

admin.site.register(ParkAppUser)
#admin.site.register(Venue)
#admin.site.register(Event)

# lists venue names alphabetically & lets an admin search by name
@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
	list_display = ('name',)
	ordering = ('name',)
	search_fields = ('name',)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
	fields = (('name', 'venue'), 'timeslot', 'description', 'host',)
	list_display = ('name', 'timeslot', 'venue',)
	list_filter = ('timeslot', 'venue',)
	ordering = ('timeslot',)