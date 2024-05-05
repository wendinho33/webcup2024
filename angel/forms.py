from django.forms import ModelForm
from angel.models import Cart, Angel

class CartForm(ModelForm):
    class Meta:
        model = Cart
        fields = ['__all__']

class AngelForm(ModelForm):
    class Meta:
        model = Angel
        fields = ['__all__']