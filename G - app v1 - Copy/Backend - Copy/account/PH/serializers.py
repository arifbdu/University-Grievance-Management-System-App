from rest_framework import serializers
from .models  import*

class pHDataSerializer(serializers.ModelSerializer):
    class Meta():
        model = pHData
        fields = "__all__"