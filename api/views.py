from django.shortcuts import render, redirect
from rest_framework import generics
from .models import Cliente, Orden, Mesa
from .serializers import ClienteSerializer, OrdenSerializer, MesaSerializer
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.

class ClienteList(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    
class OrdenList(generics.ListCreateAPIView):
    queryset = Orden.objects.all()
    serializer_class = OrdenSerializer

class OrdenDetail(generics.RetrieveAPIView):
    queryset = Orden.objects.all()
    serializer_class = OrdenSerializer
    lookup_field = 'numero'

class OrdenUpdate(generics.UpdateAPIView):
    queryset = Orden.objects.all()
    serializer_class = OrdenSerializer
    lookup_field = 'numero'

class MesaList(generics.ListCreateAPIView):
    queryset = Mesa.objects.all()
    serializer_class = MesaSerializer

class MesaDetail(generics.RetrieveAPIView):
    queryset = Mesa.objects.all()
    serializer_class = MesaSerializer
    lookup_field = 'numero'

class MesaUpdate(generics.UpdateAPIView):
    queryset = Mesa.objects.all()
    serializer_class = MesaSerializer
    lookup_field = 'numero'

class Logout(APIView):
    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)