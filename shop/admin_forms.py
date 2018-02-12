from django import forms
 
class AdminTextForm(forms.Form):
	textdata = forms.CharField(label='Товары', max_length=10000000, widget=forms.Textarea, required=True)

class AdminFileForm(forms.Form):
	filedata = forms.FileInput()
