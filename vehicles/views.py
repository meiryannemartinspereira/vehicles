from django.shortcuts import render, redirect
from vehicles.models import Vehicle
from vehicles.forms import VehicleForm

def vehicles_view(request):
    vehicles = Vehicle.objects.all().order_by('model')
    search = request.GET.get('search')

    if search:
        vehicles = vehicles.filter(model__icontains=search)

    return render(
        request,
        'vehicles.html',
        {'vehicles': vehicles}
    )

def new_vehicle_view(request):
    if request.method == 'POST':
        new_vehicle_form = VehicleForm(request.POST, request.FILES)
        if new_vehicle_form.is_valid():
            new_vehicle_form.save()
            return redirect('vehicles_list')
    else:
        new_vehicle_form = VehicleForm()
    return render(request, 'new_vehicle.html', {'new_vehicle_form': new_vehicle_form})
    
