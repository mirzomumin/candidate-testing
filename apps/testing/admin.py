from django.contrib import admin

from .models import Test, Question, Option, UserResponse, Answer
# Register your models here.


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
	list_display = ('title', 'description', 'duration_time')
	list_editable = ('duration_time',)


class InlineOption(admin.StackedInline):
	model = Option
	min_num = 2
	extra = 0


class InlineAnswer(admin.StackedInline):
	model = Answer
	extra = 0


@admin.register(UserResponse)
class UserResponseAdmin(admin.ModelAdmin):
	list_display = ('user', 'test', 'test_result_in_percent',
		'test_result', 'total_point', 'started_at', 'ended_at')
	list_filter = ('test',)
	list_select_related = ('user', 'test')
	ordering = ('test_result',)
	inlines = (
		InlineAnswer,
	)

	def total_point(self, obj):
		total_point = 0
		questions = obj.test.questions.all()
		for question in questions:
			total_point += question.point
		return total_point

	def test_result_in_percent(self, obj):
		try:
			result = round((obj.test_result / self.total_point(obj)) * 100, 2)
		except ZeroDivisionError:
			result = 0
		return result


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
	list_display = ('test', 'title', 'difficulty', 'point')
	list_editable = ('difficulty', 'point')
	list_filter = ('test',)
	inlines = (
		InlineOption,
	)