from rest_framework import serializers
from .models import Library
from django.contrib.auth.models import User
from .models import Author

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class LibrarySerializer(serializers.ModelSerializer):

    class Meta:
        model = Library
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = '__all__'