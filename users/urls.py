from django.urls import path, include
from .views import RegisterUser, UsersList
from rest_framework.routers import DefaultRouter


routers = DefaultRouter()

routers.register('', UsersList, 'users')

urlpatterns = [
    path('register/', RegisterUser.as_view(), name="register_user"),
    path('me/', include(routers.urls)),
]
