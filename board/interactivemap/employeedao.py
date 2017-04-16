from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from .models import *

class EmployeeDao:
	
	def findByName(self, name):
		return Employee.objects.filter(Q(firstName__icontains=name) | Q(lastName__icontains=name) | Q(patronym__icontains=name))
		
	def get_employee(self, id):
		try:
			return Employee.objects.get(id=id)
		except ObjectDoesNotExist as edne:
			return None		
