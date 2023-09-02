from django import forms

from crispy_bootstrap5.bootstrap5 import FloatingField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout

from .models import  Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(FloatingField('name'))
