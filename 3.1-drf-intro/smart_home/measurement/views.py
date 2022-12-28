# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import SensorDetailSerializer, SensorListSerializer, MeasurementSerializer
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, ListCreateAPIView, RetrieveAPIView, UpdateAPIView
from .models import Sensor, Measurement



class SensorsView(ListCreateAPIView):
    '''Создать датчик.Получить список всех датчиков'''
    queryset = Sensor.objects.all()
    serializer_class = SensorListSerializer


class SensorDetailView(RetrieveUpdateAPIView):
    '''Получить и изменить информацию по конкретному датчику'''
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class MeasurementView(ListCreateAPIView):
    '''Добавить измерение. Указываются ID датчика и температура.'''
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

