from django.db.models import Q
from django.db.models import Value
from django.db.models.functions import Concat
from django.core.exceptions import ObjectDoesNotExist
from .models import *

class SubdivisionDao:
	
	def get(self, id):
		try:
			return Subdivision.objects.get(id=id)
		except ObjectDoesNotExist as odne:
			return None
