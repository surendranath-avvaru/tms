# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import Book
from django.shortcuts import render
from .serializers import (
    BookSerializer,
)
from rest_framework.response import Response
from django.core import serializers
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework import permissions
# Create your views here.
class BookList(APIView):
    
    def get(self, request):
        #import pdb;pdb.set_trace()
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
