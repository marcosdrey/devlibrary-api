from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS
from core.permissions import GlobalDefaultPermission
from .serializers import BookSerializer, BookGETSerializer, BookReviewSerializer, BookGETReviewSerializer, BookSingleGETSerializer, BookReviewLikeSerializer
from .permissions import BookReviewDeletePermission
from .models import Book, BookReview


class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()

    def get_queryset(self):
        title_search = self.request.query_params.get('title', None)
        genre_search = self.request.query_params.get('genre', None)
        subgenre_search = self.request.query_params.get('subgenre', None)
        theme_search = self.request.query_params.get('theme', None)
        queryset = super().get_queryset()
        if title_search:
            queryset = queryset.filter(title__icontains=title_search)
        if genre_search:
            queryset = queryset.filter(genre__name__icontains=genre_search)
        if subgenre_search:
            queryset = queryset.filter(subgenre__name__icontains=subgenre_search)
        if theme_search:
            queryset = queryset.filter(themes__name__icontains=theme_search)
        return queryset

    def get_permissions(self):
        if self.request.method not in SAFE_METHODS:
            return [IsAuthenticated(), GlobalDefaultPermission()]
        return [IsAuthenticated()]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return BookGETSerializer
        return BookSerializer


class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()

    def get_permissions(self):
        if self.request.method not in SAFE_METHODS:
            return [IsAuthenticated(), GlobalDefaultPermission()]
        return [IsAuthenticated()]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return BookSingleGETSerializer
        return BookSerializer


class BookReviewListCreateView(generics.ListCreateAPIView):
    queryset = BookReview.objects.all()
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(user=self.request.user)

    def get_queryset(self):
        book_search = self.request.query_params.get('book', None)
        queryset = super().get_queryset()
        if book_search:
            queryset = queryset.filter(book=book_search)
        return queryset

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return BookGETReviewSerializer
        return BookReviewSerializer


class BookReviewRetrieveDestroyView(generics.RetrieveDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = BookReview.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return BookGETReviewSerializer
        return BookReviewSerializer

    def get_permissions(self):
        if self.request.method == 'DELETE':
            return [IsAuthenticated(), BookReviewDeletePermission()]
        return [IsAuthenticated()]


class BookReviewUpdateLikeView(generics.UpdateAPIView):
    queryset = BookReview.objects.all()
    serializer_class = BookReviewLikeSerializer
    permission_classes = (IsAuthenticated,)
