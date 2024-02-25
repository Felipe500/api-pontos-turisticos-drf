from django.db import IntegrityError
from rest_framework import serializers

from app.comment.models import Comment, UserLike
from app.touristic_points.models import TouristicPoint


class CommentSerializer(serializers.ModelSerializer):
    parent_id = serializers.PrimaryKeyRelatedField(
        many=False,
        required=False,
        write_only=True,
        source='parent',
        queryset=Comment.objects.all(),
    )
    touristic_point_id = serializers.PrimaryKeyRelatedField(
        many=False,
        required=True,
        write_only=True,
        source='tourist_spot',
        queryset=TouristicPoint.objects.all(),
    )
    liked = serializers.SerializerMethodField(read_only=True)
    childers = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['id', 'user_id', 'parent_id', 'touristic_point_id', 'text', 'likes', 'liked', 'childers']

    def get_childers(self, obj):
        return CommentSerializer(obj.childers, many=True, context=self.context).data

    def get_liked(self, obj):
        return UserLike.objects.filter(comment=obj, user_id=self.context.get('user_id'), liked=True).exists()

    @property
    def data(self):
        return {
            'id': self.instance.id,
            'parent_id': self.instance.parent_id,
            'user_id': self.instance.parent_id,
            'text': self.instance.text,
            'created_at': self.instance.created_at,
            'updated_at': self.instance.updated_at,
            'childers': CommentSerializer(instance=self.instance.childers, many=True, context={'request': self.context.get('request')}).data,
        }


class LikeCommentSerializer(serializers.Serializer):
    comment_id = serializers.IntegerField(required=True)
    liked = serializers.BooleanField(read_only=True)
    count_likes = serializers.IntegerField(read_only=True)

    def create(self, validated_data):
        comment = validated_data.get("comment")
        user = validated_data.get("user").id

        try:
            user_like = UserLike.objects.create(**validated_data)
            self.count_likes = comment.like()
            return user_like

        except IntegrityError:
            user_like = UserLike.objects.filter(user=user, comment=comment).first()
            if user_like.liked:
                self.count_likes = comment.unlike()
            else:
                self.count_likes = comment.like()
            user_like.liked = not user_like.liked
            user_like.save()
            return user_like

    @property
    def data(self):
        return {
            'comment_id': self.instance.comment_id,
            'liked': self.instance.liked,
            'count_likes': self.count_likes,
        }
