from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _

from rest_framework_simplejwt.tokens import RefreshToken

from app.common.models import TimeStampedModel, SoftDeletionModel
from app.common.choices import TYPE_USER, TYPE_GENDER_USER
from app.accounts.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin, TimeStampedModel, SoftDeletionModel):
    name = models.CharField(max_length=255, verbose_name=_('Nome'), null=True, blank=True)
    email = models.EmailField(max_length=255, unique=True,
                              error_messages={'unique': 'Usuário com e-mail já existente.'})
    phone = models.CharField(max_length=255, verbose_name=_('Telefone'), blank=True, null=True)
    document = models.CharField(
        max_length=40, verbose_name=_("Documento"), blank=True, null=True
    )
    gender = models.CharField(max_length=50, choices=TYPE_GENDER_USER,
                              verbose_name=_('Gênero'), blank=True, null=True)
    birth_date = models.DateField(
        verbose_name=_("Data de Nascimento"), blank=True, null=True
    )
    nationality = models.CharField(
        max_length=50, verbose_name=_("Nacionalidade"), blank=True, null=True
    )
    country = models.CharField(max_length=50, blank=True, null=True, verbose_name=_("País"))
    zipcode = models.CharField(max_length=100, blank=True, null=True, verbose_name=_('CEP'))
    city = models.CharField(max_length=50, blank=True, null=True, verbose_name=_('Cidade'))
    state = models.CharField(max_length=2, blank=True, null=True, verbose_name=_('Estado'))
    address = models.CharField(max_length=100, blank=True, null=True, verbose_name=_('Endereço'))
    number = models.CharField(max_length=10, blank=True, null=True, verbose_name=_('Número'))
    district = models.CharField(max_length=50, blank=True, null=True, verbose_name=_('Bairro'))
    complement = models.CharField(max_length=250, blank=True, null=True, verbose_name=_('Complemento'))

    agent = models.CharField(
        max_length=250, verbose_name=_("Dispositivo"), blank=True, null=True
    )

    is_staff = models.BooleanField(default=False,
                                   help_text=_('Designates whether the user can log into this admin site.'))
    is_active = models.BooleanField(
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. Unselect this instead of deleting accounts.'),
        verbose_name='Ativo?',
    )
    type = models.PositiveIntegerField(choices=TYPE_USER, blank=True, default=1, verbose_name=_('Tipo de Usuário'),
                                       editable=False)
    expires_in = models.DateField(blank=True, null=True, verbose_name='Assinatura Expira em:')
    register_ip = models.GenericIPAddressField(blank=True, null=True, verbose_name='IP de Registro')
    last_ip_login = models.GenericIPAddressField(blank=True, null=True, editable=False)
    register_agent = models.CharField(max_length=250, blank=True, null=True, verbose_name='Dispositivo')

    objects = UserManager()
    USERNAME_FIELD = 'email'

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = _("Usuário")
        verbose_name_plural = _("Todos os usuários")

    def __str__(self) -> str:
        return str(self.name)

    @property
    def owner(self):
        return self

    @property
    def refresh_token(self) -> str:
        return RefreshToken.for_user(self)

    @property
    def token(self) -> str:
        return str(self.refresh_token.access_token)

    @property
    def refresh(self) -> str:
        return str(self.refresh_token)


class ManagerUser(models.Manager):
    def __init__(self, *args, **kwargs):
        self.type = kwargs.pop('type', True)
        super().__init__(*args, **kwargs)

    def get_queryset(self):
        return super().get_queryset().filter(type=self.type)

    def create(self, **kwargs):
        kwargs.update({'type': self.type})
        return super().create(**kwargs)


class Admin(User):
    objects = ManagerUser(type=TYPE_USER.admin)

    class Meta:
        proxy = True
        verbose_name = 'Administrador'
        verbose_name_plural = 'Administradores'

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = TYPE_USER.admin
            self.is_active = True
            self.is_superuser = True
            self.is_staff = True
        super().save(*args, **kwargs)


class Customer(User):
    objects = ManagerUser(type=TYPE_USER.customer)

    class Meta:
        proxy = True
        verbose_name = 'Inscrito'
        verbose_name_plural = 'Inscritos'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

