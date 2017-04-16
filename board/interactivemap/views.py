from django.shortcuts import render
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.http import Http404
from .floordao import FloorDao
from .employeedao import EmployeeDao
from .roomdao import RoomDao

def index(request):
	dao = FloorDao()
	number = dao.get_first_floor_number()
	if not number:
		raise Http404()
	return redirect('floor', number=number)

def search(request):
	name = request.POST.get("name")
	if name:
		dao = EmployeeDao()
		employees = dao.findByName(name)
		roomDao = RoomDao()
		rooms = roomDao.findByName(name)
	else:
		employees = []
		rooms = []
	context = {
		"employees": employees,
		"num_employees_found": len(employees) if employees else 0,
		"rooms": rooms,
		"num_rooms_found": len(rooms) if rooms else 0
	}
	return render(request, 'interactivemap/search.html', context)

def floor(request, number=None):
	if not number:
		return redirect('index')
	context = {
		'floor': number,
	}
	return render(request, 'interactivemap/index.html', context)
