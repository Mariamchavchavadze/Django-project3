# myapp/forms.py
from django import forms
from .models import Vehicle


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['id','VIN', 'make', 'model', 'year', 'color', 'description' , 'image']
