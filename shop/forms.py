from django import forms
 
class BuyForm(forms.Form):
	email = forms.EmailField(label='Ваш Email', max_length=64)
	count = forms.IntegerField(label='Кол-во', min_value=1)