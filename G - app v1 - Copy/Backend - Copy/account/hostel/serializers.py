from rest_framework import serializers
from .models  import*

class HostelSerializer(serializers.ModelSerializer):
    class Meta():
        model = Hostel
        fields = "__all__"