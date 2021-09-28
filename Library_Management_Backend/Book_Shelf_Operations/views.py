from django.shortcuts import render
from.serializers import BookShelfModelSerializer
from rest_framework import viewsets
from.models import BookShelfModel
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class BookShelfViewInsert(viewsets.ModelViewSet):

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes     = [IsAuthenticated]

    serializer_class = BookShelfModelSerializer
    queryset         = BookShelfModel.objects.all()

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

class BookShelfUpdateDelete(viewsets.ModelViewSet):

    serializer_class = BookShelfModelSerializer
    queryset         = BookShelfModel.objects.all()
    lookup_field     = 'id'

    def get(self, request, id):
        if id:
            self.retrieve(request)
        else:
            self.response(status.HTTP_404_NOT_FOUND)

    def put(self, request, id=None):
        self.update(self, request, id)

    def delete(self, request, id=None):
        self.destroy(self, request, id)


