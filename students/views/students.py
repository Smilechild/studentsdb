# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse

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