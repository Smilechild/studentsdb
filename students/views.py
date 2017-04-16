# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Views for Students

def students_list(request):
	students =(
		{'id': 1,
		'first_name': u'Андрій',
		'last_name': u'Корост',
		'ticket': 2123,
		'image': 'img/01.jpg'},
		{'id': 2,
		'first_name': u'Віталій',
		'last_name': u'Подоба',
		'ticket': 254,
		'image': 'img/02.jpg'},
		{'id': 3,
		'first_name': u'Тарас',
		'last_name': u'Притула',
		'ticket': 5332,
		'image': 'img/03.jpg'},
	)
	return render(request, 'students/students_list.html',{'students': students})

def students_add(request):
	return HttpResponse('<h1>Student Add Form</h1>')

def students_edit(request, sid):
	return HttpResponse('<h1>Edit Student %s</h1>' % sid)

def students_delete(request, sid):
	return HttpResponse('<h1>Delete Student %s</h1>' % sid)

# Views for Groups

def groups_list(request):
	groups=(
		{'id': 1,
		'group_name': u'МтМ-21',
		'group_leader': u'Ячменев Олег',},
		{'id': 2,
		'group_name': u'МтМ-22',
		'group_leader': u'Віталій Подоба',},
		{'id': 3,
		'group_name': u'МтМ-23',
		'group_leader': u'Іванов Андрій',},
	)
	return render(request, 'students/groups_list.html',{'groups': groups})

def groups_add(request):
	return HttpResponse('<h1>Groups Add Form</h1>')

def groups_edit(request, gid):
	return HttpResponse('<h1>Edit Group %s</h1>' % gid)

def groups_delete(request, gid):
	return HttpResponse('<h1>Delete Group %s</h1>' % gid)