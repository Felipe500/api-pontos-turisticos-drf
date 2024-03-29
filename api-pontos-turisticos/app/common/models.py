from __future__ import annotations
from typing import List, Any
from django.utils import timezone
from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.fields import AutoCreatedField, AutoLastModifiedField


class TimeStampedModel(models.Model):
    created_at = AutoCreatedField(db_index=True, verbose_name=_('Criado em'))
    updated_at = AutoLastModifiedField(db_index=True, verbose_name=_('Modificado em'))

    class Meta:
        abstract = True


class SoftDeletionQuerySet(models.QuerySet):
    def delete(self) -> models.Model:
        return super().update(deleted_at=timezone.now())

    def hard_delete(self) -> tuple:
        return super().delete()

    def alive(self) -> List[models.Model]:
        return self.filter(deleted_at=None)

    def dead(self) -> List[models.Model]:
        return self.exclude(deleted_at=None)


class SoftDeletionManager(models.Manager):
    def __init__(self, *args: Any, **kwargs: Any):
        self.alive_only = kwargs.pop('alive_only', True)
        super().__init__(*args, **kwargs)

    def get_queryset(self) -> SoftDeletionQuerySet:
        if self.alive_only:
            return SoftDeletionQuerySet(self.model).filter(deleted_at=None)
        return SoftDeletionQuerySet(self.model)

    def hard_delete(self) -> tuple:
        return self.get_queryset().hard_delete()


class SoftDeletionModel(models.Model):
    deleted_at = models.DateTimeField(blank=True, null=True, editable=False)
    objects = SoftDeletionManager()
    all_objects = SoftDeletionManager(alive_only=False)

    class Meta:
        abstract = True

    def delete(self, using: str = None, keep_parents: bool = False) -> None:
        self.deleted_at = timezone.now()
        self.save()

    def hard_delete(self) -> None:
        super().delete()


class BaseModel(TimeStampedModel, SoftDeletionModel):
    class Meta:
        abstract = True
