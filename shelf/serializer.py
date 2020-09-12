from .models import Book
from rest_framework.serializers import ModelSerializer, BaseSerializer, ListSerializer, Serializer, HyperlinkedModelSerializer

from rest_framework import serializers


# diff between django.core.serializers - Serializes entire fields

# 1. ModelSerializer
# 2. BaseSerializer
# 3. ListSerializer
# 4. Serializer
# 5. HyperlinkedModelSerializer


class BookSerializer(ModelSerializer):   # if u used serializers.serializer then u need to write the fields as written in model.
    class Meta:
        model = Book
        fields = ('id','book_name', 'author_name', 'book_publication', 'book_qty', 'book_price')
        # fields = '__all__'
        # exclude = ('book_qty',)


# class CommentSerializer(serializers.Serializer):
#     email = serializers.EmailField()
#     content = serializers.CharField(max_length=200)
#     created = serializers.DateTimeField()





