from rest_framework import serializers
from .models import Sensor, Measurement

# TODO: опишите необходимые сериализаторы
class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        #fields = ['temperature', 'created_at']
        fields = ['sensor', 'temperature', 'created_at', 'image']

class MeasurementDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['temperature', 'created_at', 'image']

class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementDetailSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        #fields = __all__;
        fields = ['id', 'name', 'description', 'measurements']
