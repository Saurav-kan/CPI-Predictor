from rest_framework import serializers
from .models import CPIForecast

class CPIForecastSerializer(serializers.ModelSerializer):
    class Meta:
        model = CPIForecast
        fields = '__all__'
