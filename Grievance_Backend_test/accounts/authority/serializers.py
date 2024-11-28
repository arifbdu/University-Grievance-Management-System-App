from rest_framework import serializers
from .models  import*

class AuthoritySerializer(serializers.ModelSerializer):
    class Meta():
        model = Authority
        fields = "__all__"