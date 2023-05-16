from django.shortcuts import render
from django.contrib.auth import authenticate

from . serializers import *
from . models import UserModel

from rest_framework import status, generics
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
# from rest_framework
# Create your views here.

class SignUpPage(ModelViewSet):
    http_method_names = ['post']
    queryset = UserModel.objects.all()
    serializer_class = UserSignUpSerializer
    
class LoginPage(generics.GenericAPIView):
    queryset = UserModel.objects.all()
    serializer_class = LoginSerializer

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
  

        user = authenticate(email=email, password=password)

        if user is None:
            return Response({'error': 'user is not found, make sure you have signup before login in'}, status=status.HTTP_401_UNAUTHORIZED)
        
        if not user.check_password(password):
            return Response({'status': 'Fail', 'message': 'Incorrect details!!'}, status=status.HTTP_400_BAD_REQUEST)

        
        serializer = self.serializer_class(user)
        return Response({"status": 'Login successful'}, status=200)
    