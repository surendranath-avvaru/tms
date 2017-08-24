# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import Library, Author

from .serializers import (
    UserSerializer, 
    LibrarySerializer, 
    AuthorSerializer,
)
from django.contrib.auth.models import User
from rest_framework.response import Response
from django.core import serializers
from rest_framework.views import APIView
from rest_framework import status

from django.contrib.auth.decorators import permission_required
#from django.contrib.auth.mixins import PermissionRequiredMixin
print "Change1....bla bla bla"
#from rest_framework.decorators import permission_classes
#from rest_framework import permissions
# from rest_framework.decorators import permission_classes

# Create your views here.

# def users_list_view(request):
#     users = User.objects.all()
#     data = serializers.serialize('json', users,)
#     return HttpResponse(data, content_type="application/json")
#     #return HttpResponse("<h2>This is customers list</h2>")

# def libraries_list_view(request):
#     libraries = Library.objects.all()
#     data = serializers.serialize('json', libraries,)
#     return HttpResponse(data, content_type="application/json")

class UserList(APIView):

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

class LibraryList(APIView):

    def get(self, request):
        libraries = Library.objects.all()
        serializer = LibrarySerializer(libraries, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = LibrarySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from django.utils.decorators import method_decorator

from .decorators import users_have_permission

class AuthorList(APIView):
    #@method_decorator(permission_required('customers.can_update_authors'))#'customers.can_get_authors',
    @method_decorator(users_have_permission)
    def get(self, request):
        print request.user
        print request.user.has_perms(('customers.can_update_authors', 'customers.can_get_authors'))
    #if request.user.has_perm('customers.can_update_authors'):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)
        #return Response("You don't have permission to view this content")

    #@method_decorator(permission_required('customers.can_update_authors'))
    @method_decorator(users_have_permission)
    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AuthorDetail(APIView):

    def get_object(self, pk):
        try:
            return Author.objects.get(pk=pk)
        except Author.DoesNotExist:
            raise Http404

    @method_decorator(users_have_permission)
    def get(self, request, pk):
        author = self.get_object(pk)
        serializer = AuthorSerializer(author)
        return Response(serializer.data)

    @method_decorator(users_have_permission)
    def put(self, request, pk):
        author = self.get_object(pk)
        serializer = AuthorSerializer(author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @method_decorator(users_have_permission)
    def delete(self, request, pk):
        author = self.get_object(pk)
        author.delete()
        context = {'message':'Successfully deleted'}
        return Response(context)