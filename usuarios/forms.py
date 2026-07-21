from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        label='Usuário',
        max_length=50
    )

    password = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput
    )