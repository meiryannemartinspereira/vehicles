from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from vehicles.views import vehicles_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('vehicles/', vehicles_view, name='vehicles_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
