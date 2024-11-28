from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from .models import *
from .serializers import *
from rest_framework.permissions import BasePermission
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

class IsSpecificUser(BasePermission):
    email = "arif1999@gmail.com"
    password = "1999"

    def has_permission(self, request, view):
        user_model = get_user_model()
        user = authenticate(request, username=self.email, password=self.password)
        return user is not None

# Create your views here.

class GetMethod(viewsets.ModelViewSet):
    permission_classes = [IsSpecificUser, IsAuthenticated]  # Restrict access to the specific user
    queryset = pHData.objects.all()
    serializer_class = pHDataSerializer

    # ... your existing methods ...


    def list(self, request, *args, **kwargs):
        data = list(pHData.objects.all().values())
        return Response(data)

    def retrieve(self, request, *args, **kwargs):
        data = list(pHData.objects.filter(id=kwargs['pk']).values())
        return Response(data)

    def create(self, request, *args, **kwargs):
        pH_serializer_data = pHDataSerializer(data=request.data)
        if pH_serializer_data.is_valid():
            pH_serializer_data.save()
            status_code = status.HTTP_201_CREATED
            return Response({"message": "pHData Added Sucessfully", "status": status_code})
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            return Response({"message": "please fill the datails", "status": status_code})

    def destroy(self, request, *args, **kwargs):
        pH_data = pHData.objects.filter(id=kwargs['pk'])
        if pH_data:
            pH_data.delete()
            status_code = status.HTTP_201_CREATED
            return Response({"message": "pHData delete Sucessfully", "status": status_code})
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            return Response({"message": "pHData data not found", "status": status_code})

    def update(self, request, *args, **kwargs):
        pH_details = pHData.objects.get(id=kwargs['pk'])
        pH_serializer_data = pHDataSerializer(
            pH_details, data=request.data, partial=True)
        if pH_serializer_data.is_valid():
            pH_serializer_data.save()
            status_code = status.HTTP_201_CREATED
            return Response({"message": "pHData Update Sucessfully", "status": status_code})
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            return Response({"message": "pHData data Not found", "status": status_code})