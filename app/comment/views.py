from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404
from rest_framework import generics

from app.comment.models import Comment

from app.common.view import ViewCommon

from .serializers import CommentSerializer, LikeCommentSerializer


class ComentarioViewSet(ViewCommon):
    queryset = Comment.objects.filter(approved=True)
    serializer_class = CommentSerializer

    def get_object(self):
        return get_object_or_404(pk=self.kwargs.get('pk'), user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class ListComentarioViewSet(ViewCommon):
    queryset = Comment.objects.filter(approved=True, parent_id__isnull=True)
    serializer_class = CommentSerializer
    permission_classes = (AllowAny,)


class LikeInComment(generics.GenericAPIView):
    model = Comment.objects.get_queryset()
    serializer_class = LikeCommentSerializer
    queryset = model

    def post(self, *args, **kwargs) -> Response:
        comment = get_object_or_404(self.model, pk=self.kwargs.get('pk'))
        serializer = LikeCommentSerializer(data=self.request.data, context={'request': self.request})
        serializer.is_valid(raise_exception=True)
        serializer.save(user=self.request.user, comment=comment)
        return Response(serializer.data)
