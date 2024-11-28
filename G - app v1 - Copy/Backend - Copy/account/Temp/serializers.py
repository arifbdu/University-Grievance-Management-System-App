from rest_framework import serializers
from .models  import*

class TemperatureDataSerializer(serializers.ModelSerializer):
    class Meta():
        model = TemperatureData
        fields = "__all__"