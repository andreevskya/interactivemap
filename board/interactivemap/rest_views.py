from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from .models import *
from .serializers import *
from .floordao import FloorDao
from .employeedao import EmployeeDao

@api_view(['GET'])
def get_floor_numbers(request):
	dao = FloorDao()
	return Response(dao.get_floor_numbers())

@api_view(['GET'])
def get_floor(request, number):
	dao = FloorDao()
	if not number:
		number = dao.get_first_floor_number()
		if not number:
			return Response("No floors found")
	floor = dao.get_floor_by_number(number)
	if not floor:
		return Response("No floor with number %s found" % number)
	serializer = FloorSerializer(floor)
	return Response(serializer.data)
