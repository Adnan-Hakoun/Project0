from django import forms
from .models import Product





class Add_product(forms.ModelForm):
    class Meta():
        model=Product
        fields=['title','price','maker']

    # def clean_title(self):
    #     title=self.cleaned_data['title']
    #     pattern = re.compile('^[A-Za-z]+\W*[-_]*\d*')
    #     if pattern.match(title):
    #         return title
    #     return
    #
    # def clean_price(self):
    #     price=self.cleaned_data['price']
    #     if price<5:
    #         return
    #     return price
