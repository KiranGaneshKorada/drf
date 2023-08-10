from django.shortcuts import render
from . import models
from . import serializers
from rest_framework import generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class AuthorsList(generics.ListCreateAPIView):
    queryset=models.Author.objects.all()
    serializer_class=serializers.AuthorSerializer

    # LOCAL LEVEL Authentication and Authorisation goto settings.py for global level
    #authentication_classes=[BasicAuthentication]
    #permission_classes=[IsAuthenticated]


class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.Author.objects.all()
    serializer_class=serializers.AuthorSerializer

class BooksList(generics.ListCreateAPIView):
    queryset=models.Book.objects.all()
    serializer_class=serializers.BookSerializer

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.Book.objects.all()
    serializer_class=serializers.BookSerializer
