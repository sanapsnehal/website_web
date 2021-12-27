from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from events.models import client,project
from .serializers import clientserializer,projectserializer


# Create your views here.
class clientList(APIView):
    def get(self, request, format=None):
        event_api = client.objects.all()
        serializer = clientserializer(event_api, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = clientserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class clientDetail(APIView):
    def get_object(self, pk):
        try:
            return client.objects.get(pk=pk)
        except client.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        client = self.get_object(pk)
        serializer = clientserializer(client)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        client = self.get_object(pk)
        serializer = clientserializer(client, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        client = self.get_object(pk)
        serializer = clientserializer(client,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        client = self.get_object(pk)
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    

class projectList(APIView):
    def get(self, request, format=None):
        event_api = project.objects.all()
        serializer = projectserializer(event_api, many=True)
        return Response(serializer.data)

