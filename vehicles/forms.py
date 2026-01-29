from django import forms
from vehicles.models import Brand

class VehicleForm(forms.Form):
    model = forms.CharField(max_length=200)
    brand = forms.ModelChoiceField(Brand.objects.all())
    factory_year = forms.IntegerField()
    model_year = forms.IntegerField()
    plate = forms.CharField(max_length=10)
    price = forms.FloatField()
    photo = forms.ImageField()