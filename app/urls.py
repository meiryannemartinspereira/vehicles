from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import register_view, login_view, logout_view
from vehicles.views import NewVehicleView, VehiclesListView, VehicleDetailView, VehicleUpdateView, VehicleDeleteView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('vehicles/', VehiclesListView.as_view(), name='vehicles_list'),
    path('new_vehicle/', NewVehicleView.as_view(), name='new_vehicle'),
    path('vehicle/<int:pk>/', VehicleDetailView.as_view(), name='vehicle_details'),
    path('vehicle/<int:pk>/update/', VehicleUpdateView.as_view(), name='vehicle_update'),
    path('vehicle/<int:pk>/delete/', VehicleDeleteView.as_view(), name='vehicle_delete'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
