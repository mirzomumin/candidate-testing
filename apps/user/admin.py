from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm
# Register your models here.


class CustomUserAdmin(UserAdmin):
	add_form = CustomUserCreationForm
	form = CustomUserChangeForm
	model = CustomUser
	list_display = ('username', 'last_name', 'email', 'phone', 'role', 'is_active')
	fieldsets = UserAdmin.fieldsets + (
		(None, {'fields': ('phone', 'vacancies', 'resume', 'about_me', 'avatar',
			'linkedin', 'telegram', 'github', 'role')}),
	)
	add_fieldsets = (
		(None, {'fields': ('username', 'last_name', 'email', 'role', 'phone', 'password1', 'password2')}),
	)


admin.site.register(CustomUser, CustomUserAdmin)