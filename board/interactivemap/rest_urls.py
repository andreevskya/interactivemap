from django.conf.urls import url
from . import rest_views

urlpatterns = [
	url(r'floor/(?P<number>[0-9]?)$', rest_views.get_floor, name='get_floor'),
	url(r'floor/numbers', rest_views.get_floor_numbers, name='floor_numbers'),
]
