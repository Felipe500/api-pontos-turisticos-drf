from rest_framework.serializers import ModelSerializer
from app.comentarios.models import Comment


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['user', 'text', 'data', 'aprovado']
        