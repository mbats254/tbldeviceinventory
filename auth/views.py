from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import MyTokenObtainPairSerializer, RegisterSerializer, LogoutSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import api_view, parser_classes ,renderer_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser, JSONParser, FileUploadParser

# Create your views here.



class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer

class LogoutView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = LogoutSerializer
    
    
    
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer 
    # Response(serializer_class)  
    
@api_view(['GET'])
def allViews(request):
    api_urls = {
        'authenticate':'/auth/login',
        'inventory_app' :'/inventory',    
       

    }
    return Response(api_urls)
    
@api_view(['GET'])
def getUser(request):
   
    return Response(request.data['username'])