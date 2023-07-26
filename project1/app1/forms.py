from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = "__all__"
        labels = {
            'o_id': 'ORDER_ID',
            'name': 'NAME',
            'o_price' : 'O_PRICE',
            'o_date': 'O_DATE',
            'product': 'PRODUCT_NAME',
            #'phone': 'PHONE',
            'add' : 'ADDRESS'
        }
        widgets ={
            'o_id': forms.NumberInput(attrs={'class':'form-control'}),
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'o_price':forms.NumberInput(attrs={'class':'form-control'}),
            'o_date':forms.DateTimeInput(attrs={'class':'form-control','type':'date'}),
            'product': forms.TextInput(attrs={'class':'form-control'}),
            #'phone': forms.NumberInput(attrs={'class':'form-control'}),
            'add': forms.Textarea(attrs={'class':'form-control'})

        }