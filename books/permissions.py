from rest_framework.permissions import BasePermission, SAFE_METHODS
from .models import BookReview


class BookReviewDeletePermission(BasePermission):

    def has_permission(self, request, view):
        if request.method not in SAFE_METHODS:
            review_id = view.kwargs.get('pk')
            try:
                book_review = BookReview.objects.get(id=review_id)
                if book_review.user == request.user:
                    return True
                return False
            except BookReview.DoesNotExist:
                return False
