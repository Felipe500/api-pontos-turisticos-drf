from django.contrib import admin
from django.urls import include, re_path, path

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Blitz Members API",
        default_version="v1",
        description="Blitz Members®",
        terms_of_service="https://blitzpay.com.br/policies/terms/",
        contact=openapi.Contact(email="tecnologia@blitzpay.com.br"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('atracoes/', include('app.atracoes.urls')),
    path('avaliacoes/', include('app.avaliacoes.urls')),
    path('comentarios/', include('app.comentarios.urls')),
    path('enderecos/', include('app.enderecos.urls')),
    path('core/', include('app.core.urls')),
    re_path(r"^docs/$", schema_view.with_ui("redoc"), name="schema-swagger-ui"),

]
