from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# --- PERSONALIZAÇÃO DO PAINEL ---
admin.site.site_header = "Painel de Gerência (Portfólio)" # O que aparece na barra azul escura
admin.site.site_title = "Painel Administrativo" # O que aparece na aba do navegador
admin.site.index_title = "Visão Geral do Sistema" # O título central da página principal
# --------------------------------

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio.urls')),
    path('tinymce/', include('tinymce.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)