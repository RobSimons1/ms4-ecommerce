from django import forms 
from .models import Review

class ItemForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('name', 'review', 'rating', 'date',)