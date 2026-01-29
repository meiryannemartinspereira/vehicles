from django import forms
from vehicles.models import Brand, Vehicle

class VehicleForm(forms.Form):
    model = forms.CharField(max_length=200)
    brand = forms.ModelChoiceField(Brand.objects.all())
    factory_year = forms.IntegerField()
    model_year = forms.IntegerField()
    plate = forms.CharField(max_length=10)
    price = forms.FloatField()
    photo = forms.ImageField()

    def save(self):
        vehicle = Vehicle(
            model = self.cleaned_data['model'],
            brand = self.cleaned_data['brand'],
            factory_year = self.cleaned_data['factory_year'],
            model_year = self.cleaned_data['model_year'],
            plate = self.cleaned_data['plate'],
            price = self.cleaned_data['price'],
            photo = self.cleaned_data['photo']
        )

        vehicle.save()
        return vehicle