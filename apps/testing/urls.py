from django.urls import path

from testing.views.start_test import start_test
from testing.views.end_test import end_test
from testing.views.create_answer import create_answer
from testing.views.update_answer import update_answer
from testing.views.test_questions import get_test_questions
from testing.views.test_info import get_test_info
from testing.views.test_result import get_test_result

app_name = 'testing'
urlpatterns = [
	path('<int:pk>/info/', get_test_info, name='test_info'),
	path('<int:pk>/questions/', get_test_questions, name='vacancy_test'),
	path('<int:test_id>/start/', start_test, name='start_test'),
	path('<int:response_id>/end/', end_test, name='end_test'),
	path('create-question-answer/', create_answer, name='create_answer'),
	path('update-question-answer/', update_answer, name='update_answer'),
	path('<int:response_id>/result/', get_test_result, name='test_result'),
]