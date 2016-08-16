from django import forms


class BlogForm(forms.Form):
    description = forms.Textarea()
