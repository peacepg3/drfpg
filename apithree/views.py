from django.shortcuts import render
from .models import Category,Songs
from .serializer import CategSerializer,SongSerializer
from rest_framework import generics

class CategReadView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategSerializer

class DetailCategView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategSerializer


class SongReadView(generics.ListCreateAPIView):
    queryset = Songs.objects.all()
    serializer_class = SongSerializer

class DetailSongView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Songs.objects.all()
    serializer_class = SongSerializer