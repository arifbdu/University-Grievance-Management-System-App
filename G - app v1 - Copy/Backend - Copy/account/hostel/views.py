from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from django.http import JsonResponse
from .models import *
from .serializers import*
# Create your views here.

class GetMethod(viewsets.ModelViewSet):
    queryset = Hostel.objects.all()
    serializer_class = HostelSerializer

    def list(self, request, *args, **kwargs):
        data = list(Hostel.objects.all().values())
        return Response(data)

    def retrieve(self, request, *args, **kwargs):
        data = list(Hostel.objects.filter(id=kwargs['pk']).values())
        return Response(data)

    def create(self, request, *args, **kwargs):
        hostel_serializer_data = HostelSerializer(data=request.data)
        if hostel_serializer_data.is_valid():
            hostel_serializer_data.save()
            status_code = status.HTTP_201_CREATED
            return Response({"message": "Grievance Added Sucessfully", "status": status_code})
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            return Response({"message": "please fill the datails", "status": status_code})

    def destroy(self, request, *args, **kwargs):
        hostel_data = Hostel.objects.filter(id=kwargs['pk'])
        if hostel_data:
            hostel_data.delete()
            status_code = status.HTTP_201_CREATED
            return Response({"message": "Grievance delete Sucessfully", "status": status_code})
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            return Response({"message": "Grievance data not found", "status": status_code})

    def update(self, request, *args, **kwargs):
        hostel_details = Hostel.objects.get(id=kwargs['pk'])
        hostel_serializer_data = HostelSerializer(
            hostel_details, data=request.data, partial=True)
        if hostel_serializer_data.is_valid():
            hostel_serializer_data.save()
            status_code = status.HTTP_201_CREATED
            return Response({"message": "Grievance Update Sucessfully", "status": status_code})
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            return Response({"message": "Grievance data Not found", "status": status_code})