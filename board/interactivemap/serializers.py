# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import *
	
class DivisionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Division
		fields = '__all__'
		
class SubdivisionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Subdivision
		fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
	division = DivisionSerializer()
	subdivision = SubdivisionSerializer()
	post = PostSerializer(many=True)
	class Meta:
		model = Employee
		depth: 10
		exclude = ('room',)
		
class RoomSerializer(serializers.ModelSerializer):
	class Meta:
		model = Room
		exclude = ('floor',)
		depth = 10
	employees = EmployeeSerializer(many=True)
		
class FloorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Floor
		fields = '__all__'
		depth = 10
	rooms = RoomSerializer(many=True)
