from django.db.models import Q
from django.db.models import Value
from django.db.models.functions import Concat
from django.core.exceptions import ObjectDoesNotExist
from .models import *

class EmployeeDao:
	
	def findByName(self, name):
		queryset = Employee.objects.annotate(search_fullname=Concat('firstName', Value(' '), 'lastName', Value(' '), 'patronym'))
		return queryset.filter(Q(search_fullname__icontains=name))
		
	def get_employee(self, id):
		try:
			return Employee.objects.get(id=id)
		except ObjectDoesNotExist as edne:
			return None
