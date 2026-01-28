from django.contrib import admin
from vehicles.models import Vehicle, Brand


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class VehicleAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'price')
    search_fields = ('model', )

admin.site.register(Brand, BrandAdmin)
admin.site.register(Vehicle, VehicleAdmin)