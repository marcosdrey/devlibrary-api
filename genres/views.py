from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS
from core.permissions import GlobalDefaultPermission
from .serializers import GenreSerializer, GenreGETSerializer
from .models import Genre


class GenreListCreateView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GenreGETSerializer
        return GenreSerializer

    def get_permissions(self):
        if self.request.method not in SAFE_METHODS:
            return [IsAuthenticated(), GlobalDefaultPermission()]
        return [IsAuthenticated()]


class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GenreGETSerializer
        return GenreSerializer

    def get_permissions(self):
        if self.request.method not in SAFE_METHODS:
            return [IsAuthenticated(), GlobalDefaultPermission()]
        return [IsAuthenticated()]
