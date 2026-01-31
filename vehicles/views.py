from django.shortcuts import render, redirect
from vehicles.models import Vehicle
from vehicles.forms import VehicleForm

from django.views.generic import ListView, CreateView, DetailView


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


class NewVehicleView(CreateView):
    model = Vehicle
    form_class = VehicleForm
    template_name = 'new_vehicle.html'
    success_url='/vehicles/'


class VehicleDetailView(DetailView):
    model = Vehicle
    template_name = 'vehicle_detail.html'    