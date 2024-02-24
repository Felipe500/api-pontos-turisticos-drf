from rest_framework.permissions import AllowAny

from app.common.view import ViewCommon

from .models import Review
from .serializers import ReviewSerializer


class ReviewViewSet(ViewCommon):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ListReviewViewSet(ViewCommon):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (AllowAny,)
