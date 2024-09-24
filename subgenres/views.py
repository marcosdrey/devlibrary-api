from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS
from core.permissions import GlobalDefaultPermission
from .serializers import SubgenreSerializer, SubgenreGETSerializer
from .models import Subgenre


class SubgenreListCreateView(generics.ListCreateAPIView):
    queryset = Subgenre.objects.all()

    def get_permissions(self):
        if self.request.method not in SAFE_METHODS:
            return [IsAuthenticated(), GlobalDefaultPermission()]
        return [IsAuthenticated()]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return SubgenreGETSerializer
        return SubgenreSerializer


class SubgenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subgenre.objects.all()

    def get_permissions(self):
        if self.request.method not in SAFE_METHODS:
            return [IsAuthenticated(), GlobalDefaultPermission()]
        return [IsAuthenticated()]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return SubgenreGETSerializer
        return SubgenreSerializer
