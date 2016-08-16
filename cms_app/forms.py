from django import forms


class BlogForm(forms.Form):
    description = forms.Textarea()


class Register(forms.Form):
    username = forms.CharField(max_length=50)
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
