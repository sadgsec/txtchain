from django import forms

class ThreadForm(forms.Form):
    title = forms.CharField(label="Title",max_length=200)
    body  = forms.CharField(label="Body")


