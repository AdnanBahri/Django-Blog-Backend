from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework import viewsets, mixins
from rest_framework import permissions
from users.serializers import UserSerializer
from django.contrib.auth import get_user_model
User = get_user_model()


class UsersList(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser, )
    


class RegisterUser(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny,]