from django.contrib import admin

from .models import *

class EmployeeAdmin(admin.ModelAdmin):
	list_display = ('lastName', 'firstName', 'patronym', 'positions', 'room', 'visualizationBase')
	list_display_links = ('lastName', 'firstName', 'patronym')
	
	def positions(self, obj):
		return obj.get_posts()

admin.site.register(Floor)
admin.site.register(Room)
admin.site.register(Division)
admin.site.register(Subdivision)
admin.site.register(Post)
admin.site.register(Employee, EmployeeAdmin)
