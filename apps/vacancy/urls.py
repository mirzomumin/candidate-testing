from django.urls import path

from vacancy.views.vacancy_list import get_vacancy_list
from vacancy.views.vacancy_detail import get_vacancy_detail
from vacancy.views.category_list import get_category_list
from vacancy.views.apply_for_vacancy import apply_for_vacancy
from vacancy.views.vacancies_applied import get_vacancies_applied


app_name = 'vacancy'
urlpatterns = [
	path('', get_vacancy_list, name='vacancies'),
	path('<int:pk>/', get_vacancy_detail, name='vacancy'),
	path('<int:pk>/apply/', apply_for_vacancy, name='apply_for_vacancy'),
	path('categories/', get_category_list, name='categories'),
	path('applied/', get_vacancies_applied, name='vacancies_applied'),
]