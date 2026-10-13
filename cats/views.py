"""from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics"""
from rest_framework import viewsets

from .models import Cat
from .serializers import CatSerializer


class CatViewSet(viewsets.ModelViewSet):
        queryset = Cat.objects.all()
        serializer_class = CatSerializer
