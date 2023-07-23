from django.db import models
from django.contrib.auth.models import User
from datetime import date


class ParkAppUser(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	email = models.EmailField('User Email')

	def __str__(self): # lets you click on a username to access it
		return self.first_name + ' ' + self.last_name


class Venue(models.Model):
	name = models.CharField('Venue Name', max_length=120)
	description = models.TextField(blank=True)
	owner = models.IntegerField("Venue Owner", blank=False, default=1)
	venue_image = models.ImageField(null=True, blank=True, upload_to="images/")
	
	def __str__(self): # lets you click on a venue to access it
		return self.name


class Event(models.Model):
	name = models.CharField('Event Name', max_length=120)
	timeslot = models.DateTimeField('Event Date')
	venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
	# SET_NULL sets host to null if host deletes their account
	host = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL) 
	attendees = models.ManyToManyField(ParkAppUser, blank=True)
	description = models.TextField(blank=True)
	event_image = models.ImageField(null=True, blank=True, upload_to="images/")
	#fee =
	#capacity =
	#sanction_status =

	def __str__(self): # lets you click on an event name to access it
		return self.name

	@property
	def Days_till(self):
		today = date.today()
		days_till = self.timeslot.date() - today
		days_till_stripped = str(days_till).split(",", 1)[0]
		return days_till_stripped

	@property
	def Is_Past(self):
		today = date.today()
		if self.timeslot.date() < today:
			happens = "Past"
		else:
			happens = "Future"
		return happens
	