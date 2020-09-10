from django import forms
from .models import Sale, SaleDetail


class SalesForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['invoice', 'ch_no', 'purchasers', 'date']


class SalesDetailForm(forms.ModelForm):
    class Meta:
        model = SaleDetail
        fields = ['sales', 'product_name', 'created_at',
                  'quantity', 'rate', 'total', 'remarks', ]
'''
The function below is to prevent invalid input of qunatity
 s.t it is not less than quantity in Inventory 
'''

    # def clean_quantity(self):
    #     quantity = self.cleaned_data["quantity"]
    #     if quantity == 10:
    #         print(quantity)
    #         print("Error")
    #         raise forms.ValidationError("Error")
    #     return quantity
