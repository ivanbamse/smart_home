from django.urls import path
from .views import SensorDetailView, SensorUpdateView, MeasurementDetailView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensorDetailView.as_view(), name='home'),
    path('sensors/<int:pk>/', SensorUpdateView.as_view(), name='sensor'),
    path('measurements/', MeasurementDetailView.as_view(), name='measurements'),
]
