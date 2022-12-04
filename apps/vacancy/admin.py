from django.contrib import admin
from django.db.models import Q

from .models import Vacancy, Category
# Register your models here.

@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
	list_display = ('title', 'category', 'company_name', 'test',\
		'contact_person', 'phone', 'is_active')
	list_filter = ('category',)
	list_editable = ('contact_person', 'phone', 'is_active')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name', 'parent')