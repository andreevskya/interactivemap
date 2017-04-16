from django.db import models

# -*- coding: utf-8 -*-
from django.db import models

class Floor(models.Model):
	number = models.IntegerField(unique=True)
	filename = models.FileField(upload_to='maps')
	base = models.CharField(max_length=16, null=True, blank=True)
	
	def __str__(self):
		return '%s %s base: %s' % (self.filename, self.number, self.base if self.base else 'None')
		
class Room(models.Model):
	name = models.CharField(max_length=32, null=True, blank=True)
	description = models.CharField(max_length=128, null=True, blank=True)
	photo = models.ImageField(upload_to='avatars/rooms', null=True, blank=True)
	base = models.CharField(max_length=16, null=False, blank=False)
	floor = models.ForeignKey(Floor, related_name='rooms')
	
	def __str__(self):
		return '%s %s %s' % (self.name if self.name else "Unnamed", self.base, self.floor)

class Division(models.Model):
	title = models.CharField(max_length=64, null=False, blank=False)
	
	def __str__(self):
		return self.title
	
class Subdivision(models.Model):
	title = models.CharField(max_length=64, null=False, blank=False)
	division = models.ForeignKey(Division, related_name='divisions', null=False, blank=False)
	
	def __str__(self):
		return '%s of %s' % (self.title, self.division)
		
class Post(models.Model):
	title = models.CharField(max_length=64, null=False, blank=False)
	
	def __str__(self):
		return self.title

class Employee(models.Model):
	firstName = models.CharField(max_length=32, null=False, blank=False)
	lastName = models.CharField(max_length=32, null=False, blank=False)
	patronym = models.CharField(max_length=32, null=True, blank=True)
	division = models.ForeignKey(Division, null=True, blank=True, related_name='division_employees')
	subdivision = models.ForeignKey(Subdivision, null=True, blank=True, related_name='subdivision_employees')
	post = models.ManyToManyField(Post, blank=True)
	email = models.CharField(max_length=36, null=True, blank=True)
	phone = models.CharField(max_length=20, null=True, blank=True)
	phone2 = models.CharField(max_length=20, null=True, blank=True)
	avatar = models.ImageField(upload_to='avatars/employees', null=True, blank=True)
	room = models.ForeignKey(Room, related_name='employees')
	visualizationBase = models.CharField(unique=True, max_length=16, null=True, blank=True)
	deskX = models.FloatField(null=True, blank=True)
	deskY = models.FloatField(null=True, blank=True)
	
	def __str__(self):
		return '%s %s' % (self.firstName, self.lastName)
