from django import forms
from django.forms import ModelForm, fields, Form
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

class IniciarSesionForm(Form):
    username = forms.CharField(widget=forms.TextInput(), label="Usuario")
    password = forms.CharField(widget=forms.PasswordInput(), label="Contraseña")
    class Meta:
        fields = ['username', 'password']

class RegistrarUsuarioForm(UserCreationForm):
    rut = forms.CharField(max_length=80, required=True, label="Rut")
    direccion = forms.CharField(max_length=80, required=True, label="Dirección")
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'rut', 'direccion']

class PerfilUsuarioForm(Form):
    first_name = forms.CharField(max_length=150, required=True, label="Nombres")
    last_name = forms.CharField(max_length=150, required=True, label="Apellidos")
    email = forms.CharField(max_length=254, required=True, label="Correo")
    rut = forms.CharField(max_length=20, required=False, label="Rut")
    tipousu = forms.CharField(max_length=50, required=True, label="Tipo de usuario")
    dirusu = forms.CharField(max_length=300, required=False, label="Dirección")

    class Meta:
        fields = '__all__'

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ['idprod', 'nomprod', 'descprod', 'precio', 'imagen']

class Solicitud(forms.Form):
    CHOICES = [('Instalación', 'Instalación'), ('Mantención', 'Mantención'), ('Reparación', 'Reparación')]
    tipo = forms.ChoiceField(choices=CHOICES,widget=forms.Select(
    attrs={'class':'form-select', 'name': 'tipo','placeholder':'tipo:'}),
    label='Tipo solicitud')
    desc = forms.CharField(label='Descripcion', widget=forms.Textarea)
    class Meta:
        fields = ['tipo','desc','fecha']
        widgets = {'tipo': forms.TextInput(attrs={'class': 'form-control'})
                    }
        
        
class Solicitud_estado(forms.Form):
    CHOICES = [('Pendiente', 'Pendiente'), ('Cerrada', 'Cerrada'), ('Aceptada', 'Aceptada'),('Modificada', 'Modificada')]
    tipo = forms.ChoiceField(choices=CHOICES,widget=forms.Select(
    attrs={'class':'form-select', 'name': 'tipo','placeholder':'tipo:'}),
    label='Estado')
    class Meta:
        fields = ['tipo']
        widgets = {'tipo': forms.TextInput(attrs={'class': 'form-control'})
                    }        