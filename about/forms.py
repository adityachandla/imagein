from django import forms


class Contact(forms.Form):
	name = forms.CharField(max_length=100)
	information = forms.CharField(max_length=2000,widget=forms.Textarea)