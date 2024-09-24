from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS
from core.permissions import GlobalDefaultPermission
from .serializers import AuthorSerializer, AuthorGETSerializer
from .models import Author


class AuthorListCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all()

    def get_queryset(self):
        name_filter = self.request.query_params.get('name', None)
        queryset = super().get_queryset()
        if name_filter:
            queryset = queryset.filter(name__icontains=name_filter)
        return queryset

    def get_permissions(self):
        if self.request.method not in SAFE_METHODS:
            return [IsAuthenticated(), GlobalDefaultPermission()]
        return [IsAuthenticated()]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return AuthorGETSerializer
        return AuthorSerializer


class AuthorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()

    def get_permissions(self):
        if self.request.method not in SAFE_METHODS:
            return [IsAuthenticated(), GlobalDefaultPermission()]
        return [IsAuthenticated()]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return AuthorGETSerializer
        return AuthorSerializer
