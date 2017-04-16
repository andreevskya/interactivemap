from django.core.exceptions import ObjectDoesNotExist
from .models import Floor

class FloorDao:
	
	def get_first_floor_number(self):
		""" Returns first floor number from the ground."""
		number = Floor.objects.values_list('number', flat=True).order_by('number')[:1]
		if not number:
			return None
		else:
			return number[0]
			
	def get_floor_numbers(self):
		"""Returns all floor numbers"""
		return Floor.objects.values_list('number', flat=True).order_by('number')
		
	def get_floor_by_number(self, number):
		"""Returns floor by it's number or None if floor with the providen number is not found."""
		try:
			return Floor.objects.get(number=number)
		except ObjectDoesNotExist as e:
			return None
		
	
