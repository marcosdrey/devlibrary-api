from django.urls import path
from . import views


urlpatterns = [
    path('', views.ThemeListCreateView.as_view(), name='theme_list_create'),
    path('<int:pk>/', views.ThemeRetrieveUpdateDestroyView.as_view(), name='theme_rud')
]
