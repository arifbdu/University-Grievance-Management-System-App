from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from django.http import JsonResponse
from .models import *
from .serializers import*
# Create your views here.

class GetMethod(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

    def list(self, request, *args, **kwargs):
        data = list(Feedback.objects.all().values())
        return Response(data)

    def retrieve(self, request, *args, **kwargs):
        data = list(Feedback.objects.filter(id=kwargs['pk']).values())
        return Response(data)

    def create(self, request, *args, **kwargs):
        feedback_serializer_data = FeedbackSerializer(data=request.data)
        if feedback_serializer_data.is_valid():
            feedback_serializer_data.save()
            status_code = status.HTTP_201_CREATED
            return Response({"message": "Feedback Added Sucessfully", "status": status_code})
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            return Response({"message": "please fill the datails", "status": status_code})

    def destroy(self, request, *args, **kwargs):
        feedback_data = Feedback.objects.filter(id=kwargs['pk'])
        if feedback_data:
            feedback_data.delete()
            status_code = status.HTTP_201_CREATED
            return Response({"message": "Feedback delete Sucessfully", "status": status_code})
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            return Response({"message": "Feedback data not found", "status": status_code})

    def update(self, request, *args, **kwargs):
        feedback_details = Feedback.objects.get(id=kwargs['pk'])
        feedback_serializer_data = FeedbackSerializer(
            feedback_details, data=request.data, partial=True)
        if feedback_serializer_data.is_valid():
            feedback_serializer_data.save()
            status_code = status.HTTP_201_CREATED
            return Response({"message": "Feedback Update Sucessfully", "status": status_code})
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            return Response({"message": "Feedback data Not found", "status": status_code})