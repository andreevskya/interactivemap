from django.contrib import admin
from django.urls import reverse

from .models import *

class EmployeeAdmin(admin.ModelAdmin):
	view_on_site = True
	list_display = ('lastName', 'firstName', 'patronym', 'positions', 'room', 'visualizationBase')
	list_display_links = ('lastName', 'firstName', 'patronym')
	
	def positions(self, obj):
		return obj.get_posts()

	def view_on_site(self, obj):
		url = reverse("floor", kwargs={'number':obj.room.floor.number})
		return url + '#employee-' + str(obj.id)
		
admin.site.register(Floor)
admin.site.register(Room)
admin.site.register(Division)
admin.site.register(Subdivision)
admin.site.register(Post)
admin.site.register(Employee, EmployeeAdmin)
