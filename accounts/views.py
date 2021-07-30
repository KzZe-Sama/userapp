from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserView,PhoneSerializer,AddressSerializer
from .models import User,Address,Phone
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.object.all()
    serializer_class = UserView


class PhoneViewSet(viewsets.ModelViewSet):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer