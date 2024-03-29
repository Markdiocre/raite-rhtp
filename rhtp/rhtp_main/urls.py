from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from django.conf import settings

from .views import AppointmentView, ViewAppointments, ShowProviders

router = DefaultRouter()
router.register('appointment',AppointmentView)

urlpatterns = [

    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),

    path('view/appointments/', ViewAppointments.as_view()),
    path('show/providers/', ShowProviders.as_view())


] + router.urls + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
