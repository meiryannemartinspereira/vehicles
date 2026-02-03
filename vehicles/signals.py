from django.db.models.signals import pre_save, pre_delete, post_save, post_delete  
from django.dispatch import receiver
from django.db.models import Sum
from vehicles.models import Vehicle, VehicleInvetory


def vehicle_invetory_update():
    vehicles_count = Vehicle.objects.all().count()
    vehicles_price = Vehicle.objects.aggregate(
        total_price = Sum('price')
    )['total_price']

    VehicleInvetory.objects.create(
        vehicles_count = vehicles_count,
        vehicles_price = vehicles_price
    )

@receiver(post_save, sender=Vehicle)
def vehicle_post_save(sender, instance, **kwargs):
    vehicle_invetory_update()

@receiver(post_delete, sender=Vehicle)
def vehicle_post_delete(sender, instance, **kwargs):
    vehicle_invetory_update()

@receiver(pre_save, sender=Vehicle)
def vehicle_pre_save(sender, instance, **kwargs):
    print('### PRE SAVE ###')

@receiver(pre_delete, sender=Vehicle)
def vehicle_pre_delete(sender, instance, **kwargs):
    print('### PRE DELETE ###')

