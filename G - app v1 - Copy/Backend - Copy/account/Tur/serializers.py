from rest_framework import serializers
from .models  import*

class TurbidityDataSerializer(serializers.ModelSerializer):
    class Meta():
        model = TurbidityData
        fields = "__all__"