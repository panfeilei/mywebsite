from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from .serializers import FavorSerializer, InterSerializer

from .models import Favorite,Interest
# Create your views here.
class FavouViewSet(viewsets.ModelViewSet):
    serializer_class = FavorSerializer
    queryset = Favorite.objects.all()
    lookup_field = 'blogId'
    def create(self, request, *args, **kwargs):
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class InterViewSet(viewsets.ModelViewSet):
    serializer_class = InterSerializer
    queryset = Interest.objects.all()
    lookup_field = 'toUserId'