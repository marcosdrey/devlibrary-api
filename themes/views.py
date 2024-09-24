from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS
from core.permissions import GlobalDefaultPermission
from .serializers import ThemeSerializer
from .models import Theme


class ThemeListCreateView(generics.ListCreateAPIView):
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer

    def get_permissions(self):
        if self.request.method not in SAFE_METHODS:
            return [IsAuthenticated(), GlobalDefaultPermission()]
        return [IsAuthenticated()]


class ThemeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Theme.objects.all()
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    serializer_class = ThemeSerializer

    def get_permissions(self):
        if self.request.method not in SAFE_METHODS:
            return [IsAuthenticated(), GlobalDefaultPermission()]
        return [IsAuthenticated()]
