from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ParkAppUser(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	email = models.EmailField('User Email')

	def __str__(self): # lets you click on a username to access it
		return self.first_name + ' ' + self.last_name


class Venue(models.Model):
	name = models.CharField('Venue Name', max_length=120)
	description = models.TextField(blank=True)

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
	#fee =
	#capacity =
	#sanction_status =

	def __str__(self): # lets you click on an event name to access it
		return self.name