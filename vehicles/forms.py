from django import forms
from vehicles.models import Brand, Vehicle

class VehicleForm(forms.Form):
    class Meta:
        model = Vehicle
        fields = '__all__'