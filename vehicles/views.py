from django.shortcuts import render, redirect
from vehicles.models import Vehicle
from vehicles.forms import VehicleForm

from django.views.generic import ListView, View


class VehiclesListView(ListView):
    model = Vehicle
    template_name = 'vehicles.html'
    context_object_name = 'vehicles'

    def get_queryset(self):
        vehicles = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')

        if search:
            vehicles = vehicles.filter(model__icontains=search)
        return vehicles


class NewVehicleView(View):

    def get(self, request):
        vehicle_form = VehicleForm()

        return render(request, 'new_vehicle.html', {'vehicle_form': vehicle_form})
    
    def post(self, request):
        vehicle_form = VehicleForm(request.POST, request.FILES)

        if vehicle_form.is_valid():
            vehicle_form.save()
            return redirect('vehicles_list')   
        return render(request, 'new_vehicle.html', {'vehicle_form': vehicle_form})
    
