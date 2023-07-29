from django import forms
from django.forms import ModelForm
from .models import Venue, Event

# Add venue form
class VenueForm(ModelForm):
	class Meta: # Meta helps to define things in a class for Django
		model = Venue
		fields = ('name', 'description', 'venue_image')
		labels = {
			'name': '',
			'description': '',
			'venue_image': '',
		}
		widgets = {
			'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Venue Name'}),
			'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Venue Description'}),
		}


# Admin SuperUser event form
class EventFormAdmin(ModelForm):
	class Meta:
		model = Event
		fields = ('name', 'timeslot', 'venue', 'host', 'description', 'event_image')
		labels = {
			'name': '',
			'timeslot': 'YYYY-MM-DD HH:MM:SS',
			'venue': 'Venue',
			'host': 'Host',
			'description': '',
			'event_image': '',
		}
		widgets = {
			'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Event Name'}),
			'timeslot': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Event Date'}),
			'venue': forms.Select(attrs={'class':'form-select', 'placeholder':'Venue'}),
			'host': forms.Select(attrs={'class':'form-select', 'placeholder':'Host'}),
			'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Description'}),
		}


# User event form
class EventForm(ModelForm):
	class Meta:
		model = Event
		fields = ('name', 'timeslot', 'venue', 'description', 'event_image')
		labels = {
			'name': '',
			'timeslot': 'YYYY-MM-DD HH:MM:SS',
			'venue': 'Venue',
			'description': '',
			'event_image': '',
		}
		widgets = {
			'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Event Name'}),
			'timeslot': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Event Date'}),
			'venue': forms.Select(attrs={'class':'form-select', 'placeholder':'Venue'}),
			'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Description'}),
		}