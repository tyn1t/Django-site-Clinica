from django.urls import path 
from .views import RegistroViews, LoginViews, LogoutAPIView, Email, PasswordUpdateView
# from rest_framework.authtoken import views
from rest_framework_simplejwt.views import ( 
                    TokenObtainPairView,
                    TokenRefreshView
)

urlpatterns= [
    path('auth-users/login/', LoginViews.as_view(), name="Login"),
    path('auth-user/registros/', RegistroViews.as_view(), name="registro"),
    path('auth-user/update/passwork/', PasswordUpdateView.as_view(), name='UpdatePasswork'),
    path('auth-user/logout/', LogoutAPIView.as_view(), name="logout"),
    path('auth-user/registros/', RegistroViews.as_view(), name="registro"),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += [
    path("enviar/email/", Email.as_view(), name='Email'),
]