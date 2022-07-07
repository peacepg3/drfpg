from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets

class userview(viewsets.ModelViewSet):
    def list(self, request, *args, **kwargs):
        queryser = User.objects.all()
        return queryser



