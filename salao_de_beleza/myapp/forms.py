from django.forms import ModelForm
from django import forms
from myapp.models import Usuario, Comentario

class UsersForm(ModelForm):
    usuario = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Usuario',
        'maxlength':'30'
        }))

    nome = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Email',
        'maxlength':'30'
        }))

    senha = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Senha',
        'maxlength':'30'
        }))

    ultimo_nome = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'ultimo_nome',
        'maxlength':'30'
        }))

    class Meta:
        model =  Usuario
        widgets = {'password': forms.PasswordInput(),}
        fields = ['usuario', 'senha', 'nome', 'ultimo_nome']

class LoginForm(ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Usuario
        widgets = {'password': forms.PasswordInput(),}
        fields = ['usuario', 'senha']

class ComentariosForm(ModelForm):
    class Meta:
        model = Comentario
        fields = ['comentario']
