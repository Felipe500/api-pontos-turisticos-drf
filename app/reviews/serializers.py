from rest_framework.serializers import ModelSerializer
from app.avaliacoes.models import Review


class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'user', 'text', 'note', 'created_at']
        