from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import views
from django.contrib.auth import authenticate, get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


from .serializers import AppointmentsSerializer, UserSerializer
from .models import Appointments, User

User = get_user_model()

# Create your views here.
class AppointmentView(viewsets.ModelViewSet):
    queryset = Appointments.objects.all()
    permission_classes = [IsAuthenticated,]
    serializer_class = AppointmentsSerializer

    def get_queryset(self):
        return super().get_queryset().filter(patient = self.request.user)

class ViewAppointments(views.APIView):
    permission_classes = [IsAuthenticated,]

    # def get_queryset(self):
    #     return super().get_queryset().filter(provider = self.request.user)
    
    def get(self, request, format=None):
        appoints = Appointments.objects.all().filter(provider = self.request.user)
        serializer = AppointmentsSerializer(appoints, many=True)
        return Response(serializer.data)
    
class ShowProviders(views.APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request, format=None):
        providers = User.objects.all().filter(role='provider')
        print(providers)
        serializer = UserSerializer(providers, many=True)
        return Response(serializer.data)