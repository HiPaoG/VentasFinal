from django.contrib.admin import widgets
from django import forms
from .models import Compra, Usuario, Producto

class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ('usuario', 'producto',
        'cantidad','fecha')

def __init__ (self, *args, **kwargs):
    super(CompraForm, self).__init__(*args, **kwargs)
    self.fields['fecha'].widget = forms.widgets.AdminSplitDateTime()
    self.fields['usuario'].widget = forms.widgets.CheckboxSelectMultiple()
    self.fields['usuario'].help_text = "Seleccione un usuario"
    self.fields['usuario'].queryset = Usuario.objects.all()
    self.fields['producto'].widgets.CheckboxSelectMultiple()
    self.fields['producto'].help_text = "Seleccione el producto"
    self.fields['producto'].queryset = Producto.objects.all()
