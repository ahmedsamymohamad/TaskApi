
from django.contrib import admin
from django.urls import path, include
from .views import CreateUserView
from rest_framework_simplejwt.views import  (TokenRefreshView,)
from .views import MyTokenObtainPairView

urlpatterns=[
    path("api/user/register/", CreateUserView.as_view(), name="register"),
    path("api/token/", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="refresh"),
    path("api-auth/", include("rest_framework.urls")), 
]