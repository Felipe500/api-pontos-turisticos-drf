from rest_framework.permissions import AllowAny

from app.comentarios.models import Comment

from app.common.view import ViewCommon

from .serializers import CommentSerializer


class ComentarioViewSet(ViewCommon):
    queryset = Comment.objects.filter(approved=True)
    serializer_class = CommentSerializer


class ListComentarioViewSet(ViewCommon):
    queryset = Comment.objects.filter(approved=True)
    serializer_class = CommentSerializer
    permission_classes = (AllowAny,)
