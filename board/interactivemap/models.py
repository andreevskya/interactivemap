from django.db import models

# -*- coding: utf-8 -*-
from django.db import models

class Floor(models.Model):
	number = models.IntegerField(unique=True)
	filename = models.FileField(upload_to='maps')
	base = models.CharField(max_length=16, null=True, blank=True)
	
	def __str__(self):
		return '%d' % self.number
		
class Room(models.Model):
	name = models.CharField(max_length=32, null=True, blank=True)
	description = models.CharField(max_length=256, null=True, blank=True)
	photo = models.ImageField(upload_to='avatars/rooms', null=True, blank=True)
	base = models.CharField(max_length=16, null=False, blank=False)
	floor = models.ForeignKey(Floor, related_name='rooms')
	
	def __str__(self):
		return '%s on the floor %s' % (self.name if self.name else "Unnamed Room", self.floor)

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
	phone = models.CharField(max_length=26, null=True, blank=True)
	phone2 = models.CharField(max_length=26, null=True, blank=True)
	avatar = models.ImageField(upload_to='avatars/employees', null=True, blank=True)
	room = models.ForeignKey(Room, related_name='employees')
	visualizationBase = models.CharField(unique=True, max_length=16, null=True, blank=True)
	deskX = models.FloatField(null=True, blank=True)
	deskY = models.FloatField(null=True, blank=True)
	
	def get_posts(self):
		if not self.post:
			return "Unassigned"
		ps = []
		for p in self.post.all():
			ps.append(p.title)
		return ", ".join(ps)
	
	def __str__(self):
		return '%s %s' % (self.firstName, self.lastName)
