from . import models
from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Book
        fields='__all__'


class AuthorSerializer(serializers.ModelSerializer):
    # when performing crud operations not only author data but books related to author data should also be serialised
    books=BookSerializer(read_only=True,many=True)
    class Meta:
        model=models.Author
        fields='__all__'