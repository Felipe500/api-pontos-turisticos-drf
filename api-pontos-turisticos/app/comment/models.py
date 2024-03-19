from django.db import models

from app.common.models import BaseModel


class Comment(BaseModel):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    text = models.TextField()
    likes = models.PositiveIntegerField(default=0, editable=False)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, editable=False)
    tourist_spot = models.ForeignKey('touristic_points.TouristicPoint', on_delete=models.CASCADE)
    approved = models.BooleanField(default=True)

    def __str__(self):
        return str(self.user.name)

    @property
    def childers(self):
        return Comment.objects.filter(parent=self).order_by('-id')[:20]

    @property
    def total_childers(self):
        return Comment.objects.filter(parent=self).count()

    def liked(self, user_id):
        return UserLike.objects.filter(comment=self, user_id=user_id).exists()

    def like(self):
        Comment.objects.filter(pk=self.pk).update(**{'likes': models.F('likes') + 1})
        return self.likes + 1

    def unlike(self):
        Comment.objects.filter(pk=self.pk).update(**{'likes': models.F('likes') - 1})
        return self.likes - 1


class UserLike(BaseModel):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, blank=True, null=True, editable=False)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, blank=True, null=True, editable=False)
    liked = models.BooleanField(default=True, null=True)

    class Meta:
        unique_together = ['user', 'comment']
