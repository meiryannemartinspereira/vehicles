from django.shortcuts import render
from vehicles.models import Vehicle

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
