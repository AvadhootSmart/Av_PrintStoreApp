from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    TYPE_CHOICES = (
        ('B&W', 'Black and White'),
        ('Color', 'Color'),
    )
    ORIENTATION_CHOICES = (
        ('Single', 'Single Page'),
        ('Double', 'Double Page'),
    )
    name = forms.CharField(max_length=100)
    orientation = forms.ChoiceField(choices=Order.ORIENTATION_CHOICES, widget=forms.RadioSelect)
    ColorType = forms.ChoiceField(choices=Order.TYPE_CHOICES, widget=forms.RadioSelect)
    UploadFile = forms.FileField()
    
    
    class Meta:
        model = Order
        fields = ['name', 'orientation', 'ColorType', 'UploadFile', 'filename']