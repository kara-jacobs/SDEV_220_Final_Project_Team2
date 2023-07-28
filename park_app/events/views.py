from django.shortcuts import render, redirect, get_object_or_404
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from django.http import HttpResponseRedirect, HttpResponse
from .models import Event, Venue
from .forms import VenueForm, EventForm, EventFormAdmin
from django.contrib import messages
from django.urls import reverse_lazy, reverse

# Import user model from django
from django.contrib.auth.models import User 

# Import Pagination Stuff
from django.core.paginator import Paginator



# Create My Events Page
def my_events(request):
	if request.user.is_authenticated:
		me = request.user.id

		events = Event.objects.filter(host=me)
		return render(request, 
			'events/my_events.html', {"events": events
			})

	else:
		messages.success(request, ("You Aren't Authorized To View This Page"))
		return redirect('home')


########## We will probably cut this feature. 
########## Or redo it to print out details of an event instead.
# generate a text file that lists the venues
def venue_text(request):
	response = HttpResponse(content_type='text/plain')
	response['Content-Disposition'] = 'attachment; filename=venues.txt'

	lines = [] # empty list to be returned later
	venue_list = Venue.objects.all() # get the venues
	for ven in venue_list: # append them to list line by line
		lines.append(f'{ven}\n')
	
	# write the filled list to a text file
	response.writelines(lines)
	return response


# Delete a Venue
def delete_venue(request, venue_id):
	venue = Venue.objects.get(pk=venue_id)
	venue.delete()
	return redirect('list-venues')


# Delete an Event
def delete_event(request, event_id):
	event = Event.objects.get(pk=event_id)
	if request.user == event.host:
		event.delete()
		messages.success(request, ("Event Deleted!!"))
		return redirect('list-events')
	else:
		messages.success(request, ("You Aren't Authorized To Delete This Event!!!"))
		return redirect('list-events')


# Add an Event
def add_event(request):
	submitted = False # ensures nothing is posted when you first navigate to the page
	if request.method == "POST":
		if request.user.is_superuser:
			form = EventFormAdmin(request.POST, request.FILES) # passes what was posted into the Venue form for admin
			if form.is_valid():
				form.save() # if the data in the form is valid, it's saved to the database
				return HttpResponseRedirect('/add_event?submitted=True')
		else:
			form = EventForm(request.POST, request.FILES) # passes what was posted into the Venue form
			if form.is_valid():
				event = form.save(commit=False)
				event.host = request.user
				event.save()
				return HttpResponseRedirect('/add_event?submitted=True')
	else: 
		# Just Going To The Page, Not Submitting
		if request.user.is_superuser:
			form = EventFormAdmin
		else: 
			form = EventForm 
		if 'submitted' in request.GET: 
			submitted = True 
	return render(request, 'events/add_event.html', {'form':form, 'submitted':submitted})


# Update an Event
def update_event(request, event_id):
	event = Event.objects.get(pk=event_id)
	if request.user.is_superuser:
		form = EventFormAdmin(request.POST or None, request.FILES or None, instance=event)
	else:
		form = EventForm(request.POST or None, request.FILES or None, instance=event)
	if form.is_valid():
		form.save()
		return redirect('list-events')
	return render(request, 'events/update_event.html', {'event': event, 'form': form})


# Update a Venue
def update_venue(request, venue_id):
	venue = Venue.objects.get(pk=venue_id)
	form = VenueForm(request.POST or None, request.FILES or None, instance=venue) # the form is populated with the previous Venue data
	if form.is_valid():
		form.save()
		return redirect('list-venues')
	return render(request, 'events/update_venue.html', {'venue': venue, 'form': form})


# Search Through Venues
def search_venues(request):
	if request.method == "POST":
		searched = request.POST['searched']
		venues = Venue.objects.filter(name__contains=searched) # passes in whatever the user searched for
		return render(request, 'events/search_venues.html', {'searched': searched, 'venues': venues})
		return render(request, 'events/search_venues.html', {})
	else:
		return render(request, 'events/search_venues.html', {})


# Show a Venue
def show_venue(request, venue_id):
	venue = Venue.objects.get(pk=venue_id)
	venue_owner = User.objects.get(pk=venue.owner)
	return render(request, 'events/show_venue.html', {'venue': venue, 'venue_owner': venue_owner})


# List All Venues
def list_venues(request):
	# grabs all of the objects in the Venue class
	venue_list = Venue.objects.all().order_by('name') 

	# creates multiple pages for content
	p = Paginator(Venue.objects.all().order_by('name'), 8)
	page = request.GET.get('page')
	venues = p.get_page(page)
	nums = "a" * venues.paginator.num_pages

	return render(request, 'events/venue.html', 
	       				{'venue_list': venue_list,
					    'venues':venues,
					    'nums':nums
						})


# Add a Venue
def add_venue(request):
	submitted = False # ensures nothing is posted when you first navigate to the page
	if request.method == "POST":
		form = VenueForm(request.POST, request.FILES) # passes what was posted into the Venue form
		if form.is_valid():
			venue = form.save(commit=False) # doesn't save until user id is added
			venue.owner = request.user.id # logged in user
			venue.save()
			return HttpResponseRedirect('/add_venue?submitted=True')
	else: # if the form is submitted, submitted will be equal to True
		form = VenueForm
		if 'submitted' in request.GET:
			submitted = True
	return render(request, 'events/add_venue.html', {'form':form, 'submitted':submitted})


def all_events(request):
	# grabs all of the objects in the Event class
	event_list = Event.objects.all().order_by('timeslot')
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

	# Query the Events Model For Dates
	event_list = Event.objects.filter(
		timeslot__year = year, 
		timeslot__month = month_number)

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
	"event_list": event_list,
	})


def event_attend(request, pk):
	if request.user.is_authenticated:
		event = get_object_or_404(Event, id=pk)
		if event.attendance.filter(id=request.user.id):
			event.attendance.remove(request.user)
			messages.success(request, ("Your RSVP has been cancelled."))
		else:
			event.attendance.add(request.user)
			messages.success(request, ("RSVP successful. See you soon!"))
		return redirect('list-events')

	else:
		messages.success(request, ("Please Log In to Continue."))
		return redirect('home')