from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from user.views.sign_up import sign_up
from user.views.sign_in import sign_in
from user.views.sign_out import sign_out
from user.views.get_profile import get_profile
from user.views.update_profile import update_profile
from user.views.confirm_email import confirm
from user.views.change_password import change_password
from user.views.reset_password import (
    send_reset_password_instruction,
    reset_password)
from user.views.delete_user import delete_user

app_name = 'user'

urlpatterns = [
    path('sign-up/', sign_up, name="sign_up"),
    path('sign-in/', sign_in, name="sign_in"),
    path('sign-out/', sign_out, name="sign_out"),
    path('update-profile/<int:user_id>/', update_profile, name='update_profile'),
    path('get-profile/<int:user_id>/', get_profile, name='get_profile'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('confirm/', confirm, name='confirm'),
    path('password-change/', change_password, name='change_password'),
    path('password-reset/', send_reset_password_instruction,
        name='send_password_reset_instruction'),
    path('password-reset/complete/', reset_password,
        name='password_reset_complete'),
    path('delete/', delete_user, name='delete_user'),
]