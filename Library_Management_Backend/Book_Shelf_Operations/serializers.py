from rest_framework import serializers
from .models import BookShelfModel
from rest_framework import status
from rest_framework.response import Response

class BookShelfModelSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        title = validated_data['Title']
        BookExists = BookShelfModel.objects.filter(Title__iexact = title)
        if BookExists:
            raise serializers.ValidationError("Book Exist Already")

        return super().create(validated_data)

    class Meta:
        model  = BookShelfModel
        fields = ['id', 'Title', 'Category', 'Author', 'ISBN', 'Inshelf']