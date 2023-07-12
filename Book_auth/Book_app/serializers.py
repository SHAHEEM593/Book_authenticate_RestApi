from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Book

User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={"input_type": "password"})

    class Meta:
        model = User
        fields = ["id","email", "username", "password"]

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data["email"],
            username=validated_data["username"],
            password=validated_data["password"]
        )
        return user



class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'description', 'author', 'price']

    def get_read_only_fields(self):
        read_only_fields = super().get_read_only_fields()
        read_only_fields.extend(['id', 'author'])

        return read_only_fields
