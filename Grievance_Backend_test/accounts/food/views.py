from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from django.http import JsonResponse
from .models import *
from .serializers import*
# Create your views here.

class GetMethod(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

    def list(self, request, *args, **kwargs):
        data = list(Food.objects.all().values())
        return Response(data)

    def retrieve(self, request, *args, **kwargs):
        data = list(Food.objects.filter(id=kwargs['pk']).values())
        return Response(data)

    def create(self, request, *args, **kwargs):
        Food_serializer_data = FoodSerializer(data=request.data)
        if Food_serializer_data.is_valid():
            Food_serializer_data.save()
            status_code = status.HTTP_201_CREATED
            return Response({"message": "Grievance Added Sucessfully", "status": status_code})
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            return Response({"message": "please fill the datails", "status": status_code})

    def destroy(self, request, *args, **kwargs):
        Food_data = Food.objects.filter(id=kwargs['pk'])
        if Food_data:
            Food_data.delete()
            status_code = status.HTTP_201_CREATED
            return Response({"message": "Grievance delete Sucessfully", "status": status_code})
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            return Response({"message": "Grievance data not found", "status": status_code})

    def update(self, request, *args, **kwargs):
        Food_details = Food.objects.get(id=kwargs['pk'])
        Food_serializer_data = FoodSerializer(
            Food_details, data=request.data, partial=True)
        if Food_serializer_data.is_valid():
            Food_serializer_data.save()
            status_code = status.HTTP_201_CREATED
            return Response({"message": "Grievance Update Sucessfully", "status": status_code})
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            return Response({"message": "Grievance data Not found", "status": status_code})