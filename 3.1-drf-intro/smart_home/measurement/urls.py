from django.urls import path
from measurement.views import * 

urlpatterns = [
    path('sensors/', SensorsView.as_view()),
    path('sensors/<pk>/', SensorDetailView.as_view()),
    path('measurements/', MeasurementView.as_view())
]
