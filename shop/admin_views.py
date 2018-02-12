from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse

from shop.models import Goods, Category
from django.contrib import admin
from shop.admin_forms import AdminTextForm, AdminFileForm



@staff_member_required
def goods_mass_load(request):
	context = { 'title': 'Массовая загрузка товара',
				'form_text': AdminTextForm,
				'form_file': AdminFileForm,
			}
	return render(request, 'mass_load.html', context)


@staff_member_required
def goods_textform(request):
	return HttpResponse('Text Added')


@staff_member_required
def goods_fileform(request):
	return HttpResponse('File Added')