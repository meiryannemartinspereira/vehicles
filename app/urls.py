from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import register_view, login_view, logout_view
from vehicles.views import new_vehicle_view, vehicles_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('vehicles/', vehicles_view, name='vehicles_list'),
    path('new_vehicle/', new_vehicle_view, name='new_vehicle'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
