
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('^auth/', include('djoser.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/token/', include('djoser.urls.authtoken')),
    path('ap/v1/',include('app.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)