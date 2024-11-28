from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .models import *
from .serializers import*
# Create your views here.


class GetMethod(viewsets.ModelViewSet):
    queryset = TurbidityData.objects.all()
    serializer_class = TurbidityDataSerializer

    def list(self, request, *args, **kwargs):
        data = list(TurbidityData.objects.all().values())
        return Response(data)

    def retrieve(self, request, *args, **kwargs):
        data = list(TurbidityData.objects.filter(id=kwargs['pk']).values())
        return Response(data)

    def create(self, request, *args, **kwargs):
        Turbidity_serializer_data = TurbidityDataSerializer(data=request.data)
        if Turbidity_serializer_data.is_valid():
            Turbidity_serializer_data.save()
            status_code = status.HTTP_201_CREATED
            return Response({"message": "TurbidityData Added Sucessfully", "status": status_code})
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            return Response({"message": "please fill the datails", "status": status_code})

    def destroy(self, request, *args, **kwargs):
        Turbidity_data = TurbidityData.objects.filter(id=kwargs['pk'])
        if Turbidity_data:
            Turbidity_data.delete()
            status_code = status.HTTP_201_CREATED
            return Response({"message": "TurbidityData delete Sucessfully", "status": status_code})
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            return Response({"message": "Turbidity data not found", "status": status_code})

    def update(self, request, *args, **kwargs):
        Turbidity_details = TurbidityData.objects.get(id=kwargs['pk'])
        Turbidity_serializer_data = TurbidityDataSerializer(
            Turbidity_details, data=request.data, partial=True)
        if Turbidity_serializer_data.is_valid():
            Turbidity_serializer_data.save()
            status_code = status.HTTP_201_CREATED
            return Response({"message": "TurbidityData Update Sucessfully", "status": status_code})
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            return Response({"message": "Turbidity data Not found", "status": status_code})