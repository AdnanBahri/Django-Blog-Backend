from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/', include('posts.urls')),
    path('api/users/login/', TokenObtainPairView.as_view()),
    path('api/users/refresh/', TokenRefreshView.as_view()),
]
