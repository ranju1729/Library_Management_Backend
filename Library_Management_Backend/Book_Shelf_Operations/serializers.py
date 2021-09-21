from rest_framework import serializers
from .models import BookShelfModel

class BookShelfModelSerializer(serializers.ModelSerializer):
    class Meta:
        model  = BookShelfModel
        fields = ['id', 'Title', 'Category', 'Author', 'ISBN', 'Inshelf']
