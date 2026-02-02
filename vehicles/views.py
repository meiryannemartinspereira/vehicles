from django.shortcuts import render, redirect
from vehicles.models import Vehicle
from vehicles.forms import VehicleForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.urls import reverse_lazy

from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView


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
    
class VehicleDetailView(DetailView):
    model = Vehicle
    template_name = 'vehicle_detail.html'  

@method_decorator(login_required(login_url='login'), name='dispatch')
class NewVehicleView(CreateView):
    model = Vehicle
    form_class = VehicleForm
    template_name = 'new_vehicle.html'
    success_url='/vehicles/'

@method_decorator(login_required(login_url='login'), name='dispatch')
class VehicleUpdateView(UpdateView):
    model = Vehicle
    form_class = VehicleForm
    template_name = 'vehicle_update.html'
    
    def get_success_url(self):
        return reverse_lazy('vehicle_details', kwargs={'pk': self.object.pk})

@method_decorator(login_required(login_url='login'), name='dispatch')
class VehicleDeleteView(DeleteView):
    model = Vehicle
    template_name = 'vehicle_delete.html'
    success_url = '/vehicles/'