from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .models import *
from .serializers import*
# Create your views here.


class GetMethod(viewsets.ModelViewSet):
    queryset = TemperatureData.objects.all()
    serializer_class = TemperatureDataSerializer

    def list(self, request, *args, **kwargs):
        data = list(TemperatureData.objects.all().values())
        return Response(data)

    def retrieve(self, request, *args, **kwargs):
        data = list(TemperatureData.objects.filter(id=kwargs['pk']).values())
        return Response(data)

    def create(self, request, *args, **kwargs):
        Temperature_serializer_data = TemperatureDataSerializer(data=request.data)
        if Temperature_serializer_data.is_valid():
            Temperature_serializer_data.save()
            status_code = status.HTTP_201_CREATED
            return Response({"message": "TemperatureData Added Sucessfully", "status": status_code})
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            return Response({"message": "please fill the datails", "status": status_code})

    def destroy(self, request, *args, **kwargs):
        Temperature_data = TemperatureData.objects.filter(id=kwargs['pk'])
        if Temperature_data:
            Temperature_data.delete()
            status_code = status.HTTP_201_CREATED
            return Response({"message": "TemperatureData delete Sucessfully", "status": status_code})
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            return Response({"message": "Temperature data not found", "status": status_code})

    def update(self, request, *args, **kwargs):
        Temperature_details = TemperatureData.objects.get(id=kwargs['pk'])
        Temperature_serializer_data = TemperatureDataSerializer(
            Temperature_details, data=request.data, partial=True)
        if Temperature_serializer_data.is_valid():
            Temperature_serializer_data.save()
            status_code = status.HTTP_201_CREATED
            return Response({"message": "TemperatureData Update Sucessfully", "status": status_code})
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            return Response({"message": "Temperature data Not found", "status": status_code})