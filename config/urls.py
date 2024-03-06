from django.contrib import admin
from django.urls import include, re_path, path

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="PONTOS TURISTICOS API",
        default_version="v1",
        contact=openapi.Contact(email="felipe.brx.dev@gmail.com"),
        license=openapi.License(name="GNU General Public License (GNU GPL)"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('accounts/', include('app.accounts.urls')),
    path('atracoes/', include('app.attractions.urls')),
    path('avaliacoes/', include('app.reviews.urls')),
    path('comentarios/', include('app.comment.urls')),
    path('pontos-turisticos/', include('app.touristic_points.urls')),
    re_path(r"^docs/$", schema_view.with_ui("redoc"), name="schema-swagger-ui"),

]
