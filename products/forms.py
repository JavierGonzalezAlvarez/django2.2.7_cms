from django import forms
from .models import Product, NutritionalValues
from django.forms import ModelForm

class Class_Product_Form(forms.ModelForm):
    #Especificamos los datos generales con los que vamos a trabajar
    class Meta:        
        model = Product
        fields = ['name','description','nutritional_values','status']        
        labels = {'name':"Name",'description':"Description",'nutritional_values':"Nutritionla Values",'status':"Status"}       
        widget = {'name': forms.TextInput}        
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for campos_a_recorrer in iter(self.fields):
            self.fields[campos_a_recorrer].widget.attrs.update({
                'class': 'form-control'
            })

class Class_NutritionalValues_Form(forms.ModelForm):
    class Meta:
        model = NutritionalValues
        fields = ['name','unit']        
        labels = {'name':"name",'unit':"unit"}       
        widget = {'name': forms.TextInput}

    def __init__(self, *args, **kwargs):        
        super().__init__(*args, **kwargs)
        for campos_a_recorrer in iter(self.fields):
            self.fields[campos_a_recorrer].widget.attrs.update({
                'class': 'form-control'
            })
            