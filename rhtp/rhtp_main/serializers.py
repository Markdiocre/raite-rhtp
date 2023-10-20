from rest_framework import serializers
from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer, UserSerializer as BaseUserSerializer
from django.contrib.auth.models import User

from .models import Appointments

class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    class Meta(BaseUserRegistrationSerializer.Meta):
        fields = ('first_name','last_name','middle_name','phone_number','address','gender', 'is_staff','is_active')

class UserSerializer(BaseUserSerializer):
    class Meta:
        model = User
        fields = ['first_name','last_name','middle_name','phone_number','address','gender', 'is_staff','is_active']

class AppointmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointments
        fields = '__all__'