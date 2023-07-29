from django.db import models
from django.contrib.auth.models import User
from datetime import date


# Park App User Class
class ParkAppUser(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	email = models.EmailField('User Email')

	# Lets you click on a username to access it
	def __str__(self): 
		return self.first_name + ' ' + self.last_name

# Venue Class
class Venue(models.Model):
	name = models.CharField('Venue Name', max_length=120)
	description = models.TextField(blank=True)
	owner = models.IntegerField("Venue Owner", blank=False, default=1)
	venue_image = models.ImageField(null=True, blank=True, upload_to="images/")
	
	def __str__(self): # lets you click on a venue to access it
		return self.name

# Event Class
class Event(models.Model):
	name = models.CharField('Event Name', max_length=120)
	timeslot = models.DateTimeField('Event Date')
	venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
	# SET_NULL sets host to null if host deletes their account
	host = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL) 
	attendees = models.ManyToManyField(ParkAppUser, blank=True)
	description = models.TextField(blank=True)
	event_image = models.ImageField(null=True, blank=True, upload_to="images/")
	attendance = models.ManyToManyField(User, related_name='attend', blank=True)

	# Lets you click on an event name to access it
	def __str__(self): 
		return self.name

	# Shows how many days are left until the event
	@property
	def Days_till(self):
		today = date.today()
		days_till = self.timeslot.date() - today
		days_till_stripped = str(days_till).split(",", 1)[0]
		return days_till_stripped

	# Shows whether the event already occurred or not
	@property
	def Is_Past(self):
		today = date.today()
		if self.timeslot.date() < today:
			happens = "Past"
		else:
			happens = "Future"
		return happens

	# Keeps track of the number of people attending
	def number_of_attends(self):
		return self.attendance.count()
	