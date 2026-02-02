from django.db.models.signals import pre_save, pre_delete, post_save, post_delete  
from django.dispatch import receiver
from vehicles.models import Vehicle


@receiver(pre_save, sender=Vehicle)
def vehicle_pre_save(sender, instance, **kwargs):
    print('### PRE SAVE ###')


@receiver(post_save, sender=Vehicle)
def vehicle_post_save(sender, instance, **kwargs):
    print('### POS SAVE ###')

@receiver(pre_delete, sender=Vehicle)
def vehicle_pre_delete(sender, instance, **kwargs):
    print('### PRE DELETE ###')

@receiver(post_delete, sender=Vehicle)
def vehicle_post_delete(sender, instance, **kwargs):
    print('### POS DELETE ###')