from django import forms

class PathForm(forms.Form):
    source_path = forms.CharField(label='Source Path', max_length=255)
    destination_path = forms.CharField(label='Destination Path', max_length=255)
