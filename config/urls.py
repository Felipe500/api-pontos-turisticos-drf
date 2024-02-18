from django.contrib import admin
from django.urls import include, re_path, path


urlpatterns = [
    path("admin/", admin.site.urls),
    path('atracoes/', include('app.atracoes.urls')),
    path('avaliacoes/', include('app.avaliacoes.urls')),
    path('comentarios/', include('app.comentarios.urls')),
    path('enderecos/', include('app.enderecos.urls')),
    path('core/', include('app.core.urls')),
]
