from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.serializers import ValidationError
from app.common.view import ViewCommon

from .models import Review
from .serializers import ReviewSerializer


class ReviewViewSet(ViewCommon):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_object(self):
        return get_object_or_404(self.queryset, pk=self.kwargs.get('pk'), user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    def perform_destroy(self, instance):
        instance.delete()


class ListReviewViewSet(ViewCommon):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (AllowAny,)
