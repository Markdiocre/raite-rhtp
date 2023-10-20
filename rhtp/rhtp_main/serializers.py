from rest_framework import serializers
from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer, UserSerializer as BaseUserSerializer
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


from .models import Appointments

User = get_user_model()
class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    class Meta(BaseUserRegistrationSerializer.Meta):
        fields = ('email','first_name','last_name','middle_name','role','phone_number','address','gender', 'is_staff','is_active','password')

class UserSerializer(BaseUserSerializer):
    class Meta:
        model = User
        fields = ['first_name','last_name','middle_name','role','phone_number','address','gender']

class AppointmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointments
        fields = '__all__'