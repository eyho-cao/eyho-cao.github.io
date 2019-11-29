from django import forms
from contracts.models import Contract

class GenerateContract(forms.ModelForm):
    class Meta():
        model = Contract
        fields = '__all__'
        
