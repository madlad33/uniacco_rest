from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .serializers import UserSerializer, AuthTokenSerializer
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import exceptions, generics
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from ipaddress import ip_address, ip_network
# from ipware import get_client_ip
from django.http import HttpResponse
from rest_framework.authtoken.models import Token
import requests
from django.views.decorators.csrf import csrf_exempt
import json
from .models import UserLoginHistory


# Create your views here.
class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user"""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        self.send_data(request)
        self.save_ip(request)
        return Response({
            'token': token.key
        })

    def send_data(self, request):
        # Sends post request to the given url with user and ip address
        ip = request.META.get("REMOTE_ADDR")  # Get user's ip address
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        payload = {
            "user": user.pk,
            "ip": ip,
        }
        data = json.dumps(payload)  # Payload converted to json format
        r = requests.post("https://encrusxqoan0b.x.pipedream.net",
                          data=data)  # Post request to the given url with payload data
        return r

    def save_ip(self, request):
        # Function to save the current ip address of the user after authenticating
        ip = request.META.get("REMOTE_ADDR")  # Get user's ip address
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        UserLoginHistory.objects.create(ip=ip,
                                        user=user)  # Create entry in the user login history model to save the
        # current ip
