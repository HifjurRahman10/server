from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import *
from rest_framework.permissions import IsAuthenticated , AllowAny


# Create your views here.
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class CreateShortVideo(generics.ListCreateAPIView):
    serializer_class = ShortVideoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return ShortVideo.objects.filter(userId = user)
    
    def prerfom_create(self, serializer):
        if serializer.is_valid():
            serializer.save(userId=self.request.user)
        else:
            print(serializer.errors)

class DeleteShortVideo(generics.DestroyAPIView):
    serializer_class = ShortVideoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return ShortVideo.objects.filter(userId = user)