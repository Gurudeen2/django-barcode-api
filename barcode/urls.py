from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('qrbarcode.urls') )
]
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
key='django-insecure-h_b887k+ys6#w^*1l!%1&$9t6(hk2ij&#9eo7a(_-z#4az26=s'