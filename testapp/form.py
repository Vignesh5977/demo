from django import forms
from .models import allData

class datafrom(forms.ModelForm):
    date = forms.DateField(
        input_formats=['%d/%m/%Y', '%Y-%m-%d'],
        error_messages={
            'invalid': 'Please enter a valid date (format: DD/MM/YYYY or YYYY-MM-DD).'
        }
    )
    class Meta:
        model = allData
        fields = '__all__'