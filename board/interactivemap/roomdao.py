from django.db.models import Q
from .models import *

class RoomDao:
	
	def findByName(self, name):
		return Room.objects.filter(Q(name__icontains=name))
