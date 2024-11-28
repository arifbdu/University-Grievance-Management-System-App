from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from django.http import JsonResponse
from .models import *
from .serializers import*
# Create your views here.

class GetMethod(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer

    def list(self, request, *args, **kwargs):
        data = list(Certificate.objects.all().values())
        return Response(data)

    def retrieve(self, request, *args, **kwargs):
        data = list(Certificate.objects.filter(id=kwargs['pk']).values())
        return Response(data)

    def create(self, request, *args, **kwargs):
        Certificate_serializer_data = CertificateSerializer(data=request.data)
        if Certificate_serializer_data.is_valid():
            Certificate_serializer_data.save()
            status_code = status.HTTP_201_CREATED
            return Response({"message": "Grievance Added Sucessfully", "status": status_code})
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            return Response({"message": "please fill the datails", "status": status_code})

    def destroy(self, request, *args, **kwargs):
        Certificate_data = Certificate.objects.filter(id=kwargs['pk'])
        if Certificate_data:
            Certificate_data.delete()
            status_code = status.HTTP_201_CREATED
            return Response({"message": "Grievance delete Sucessfully", "status": status_code})
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            return Response({"message": "Grievance data not found", "status": status_code})

    def update(self, request, *args, **kwargs):
        Certificate_details = Certificate.objects.get(id=kwargs['pk'])
        Certificate_serializer_data = CertificateSerializer(
            Certificate_details, data=request.data, partial=True)
        if Certificate_serializer_data.is_valid():
            Certificate_serializer_data.save()
            status_code = status.HTTP_201_CREATED
            return Response({"message": "Grievance Update Sucessfully", "status": status_code})
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            return Response({"message": "Grievance data Not found", "status": status_code})