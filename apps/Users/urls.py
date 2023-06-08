from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from apps.Users.views.login import LoginUser
from apps.Users.views.register import CreateUser
from apps.Users.views.confirm_user import ConfirmUser
from apps.Users.views.password_recovery import PasswordRecoveryView

urlpatterns = [
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', CreateUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('confirm/', ConfirmUser.as_view(), name='confirm-user'),
    path('recover/', PasswordRecoveryView.as_view(), name='password-recovery')
]
