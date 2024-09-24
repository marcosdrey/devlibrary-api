from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS
from core.permissions import GlobalDefaultPermission
from .serializers import PublisherSerializer
from .models import Publisher


class PublisherListCreateView(generics.ListCreateAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAuthenticated(), GlobalDefaultPermission()]
        return [IsAuthenticated()]


class PublisherRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

    def get_permissions(self):
        if self.request.method not in SAFE_METHODS:
            return [IsAuthenticated(), GlobalDefaultPermission()]
        return [IsAuthenticated()]
