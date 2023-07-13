from django.shortcuts import render, redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from django.http import HttpResponseRedirect
from .models import Event, Venue
from .forms import VenueForm, EventForm

# Create your views here.


def add_event(request):
	submitted = False # ensures nothing is posted when you first navigate to the page
	if request.method == "POST":
		form = EventForm(request.POST) # passes what was posted into the Venue form
		if form.is_valid():
			form.save() # if the data in the form is valid, it's saved to the database
			return HttpResponseRedirect('/add_event?submitted=True')
	else: # if the form is submitted, submitted will be equal to True
		form = EventForm
		if 'submitted' in request.GET:
			submitted = True
	return render(request, 'events/add_event.html', {'form':form, 'submitted':submitted})


def update_event(request, event_id):
	event = Event.objects.get(pk=event_id)
	form = EventForm(request.POST or None, instance=event)
	if form.is_valid():
		form.save()
		return redirect('list-events')
	return render(request, 'events/update_event.html', {'event': event, 'form': form})


def update_venue(request, venue_id):
	venue = Venue.objects.get(pk=venue_id)
	form = VenueForm(request.POST or None, instance=venue) # the form is populated with the previous Venue data
	if form.is_valid():
		form.save()
		return redirect('list-venues')
	return render(request, 'events/update_venue.html', {'venue': venue, 'form': form})


def search_venues(request):
	if request.method == "POST":
		searched = request.POST['searched']
		venues = Venue.objects.filter(name__contains=searched) # passes in whatever the user searched for
		return render(request, 'events/search_venues.html', {'searched': searched, 'venues': venues})
		return render(request, 'events/search_venues.html', {})
	else:
		return render(request, 'events/search_venues.html', {})


def show_venue(request, venue_id):
	venue = Venue.objects.get(pk=venue_id)
	return render(request, 'events/show_venue.html', {'venue': venue})


def list_venues(request):
	venue_list = Venue.objects.all() # grabs all of the objects in the Venue class
	return render(request, 'events/venue.html', {'venue_list': venue_list})


def add_venue(request):
	submitted = False # ensures nothing is posted when you first navigate to the page
	if request.method == "POST":
		form = VenueForm(request.POST) # passes what was posted into the Venue form
		if form.is_valid():
			form.save() # if the data in the form is valid, it ets saved to the database
			return HttpResponseRedirect('/add_venue?submitted=True')
	else: # if the form is submitted, submitted will be equal to True
		form = VenueForm
		if 'submitted' in request.GET:
			submitted = True
	return render(request, 'events/add_venue.html', {'form':form, 'submitted':submitted})


def all_events(request):
	event_list = Event.objects.all() # grabs all of the objects in the Event class
	return render(request, 'events/event_list.html', {'event_list': event_list})


def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')): # Year & month are dynamically updated
	name = "John"
	month = month.capitalize() # converts month name in the url to title case

	# Convert month from name to number
	month_number = list(calendar.month_name).index(month)
	month_number = int(month_number) # ensures month number is an integer

	# Create a calendar
	cal = HTMLCalendar().formatmonth(year, month_number)

	# Get current year
	now = datetime.now()
	current_year = now.year

	# Get current time
	time = now.strftime('%I:%M %p')

	return render(request, 
	'events/home.html', {
	"name": name,
	"year": year,
	"month": month,
	"month_number": month_number,
	"cal": cal,
	"current_year": current_year,
	"time": time,
	})