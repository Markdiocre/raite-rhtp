from django.shortcuts import render

from rest_framework import viewsets
from django.contrib.auth import authenticate, get_user_model
from rest_framework.permissions import IsAuthenticated


from .serializers import AppointmentsSerializer
from .models import Appointments

User = get_user_model()

# Create your views here.
class AppointmentView(viewsets.ModelViewSet):
    queryset = Appointments.objects.all()
    permission_classes = [IsAuthenticated,]
    serializer_class = AppointmentsSerializer

    def get_queryset(self):
        return super().get_queryset().filter(patient = self.request.user)
    