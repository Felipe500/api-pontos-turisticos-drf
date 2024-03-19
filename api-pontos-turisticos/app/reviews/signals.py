from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Review


@receiver(post_save, sender=Review)
def review_post_save(sender, instance, created, **kwargs):
    if created:
        Review.objects.create_review(instance.tourist_spot.id, instance.note)


@receiver(post_delete, sender=Review)
def review_post_delete(sender, instance, **kwargs):
    instance.objects.delete_review()
