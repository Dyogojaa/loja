from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

urlpatterns = [
    path('', include('produto.urls')),    
    path('perfil/', include('perfil.urls')),    
    path('pedido/', include('pedido.urls')),    
    path('admin/', admin.site.urls),    
    
] +static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    
    urlpatterns = [
    path("__debug__/", include("debug_toolbar.urls")),
    
    
] + urlpatterns

    
