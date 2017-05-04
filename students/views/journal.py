# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse

def journal(request):
	journal=(
		{'id': 1,
		'name': u'Корост Андрій',},
		{'id': 2,
		'name': u'Подоба Віталій',},
		{'id': 3,
		'name': u'Притула Тарас',},
	)
	return render(request, 'students/journal.html', {'journal': journal})