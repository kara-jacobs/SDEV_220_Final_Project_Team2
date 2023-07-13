from django import forms
from django.forms import ModelForm
from .models import Venue, Event

# Add venue form
class VenueForm(ModelForm):
	class Meta: # Meta helps to define things in a class for Django
		model = Venue
		fields = ('name', 'description',)
		labels = {
			'name': '',
			'description': '',
		}
		widgets = {
			'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Venue Name'}),
			'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Venue Description'}),
		}


# Add event form
class EventForm(ModelForm):
	class Meta:
		model = Event
		fields = ('name', 'timeslot', 'venue', 'host', 'attendees', 'description')
		labels = {
			'name': '',
			'timeslot': 'YYYY-MM-DD HH:MM:SS',
			'venue': 'Venue',
			'host': 'Host',
			'attendees': 'Attendees',
			'description': '',
		}
		widgets = {
			'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Event Name'}),
			'timeslot': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Event Date'}),
			'venue': forms.Select(attrs={'class':'form-select', 'placeholder':'Venue'}),
			'host': forms.Select(attrs={'class':'form-select', 'placeholder':'Host'}),
			'attendees': forms.SelectMultiple(attrs={'class':'form-control', 'placeholder':'Attendees'}),
			'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Description'}),
		}