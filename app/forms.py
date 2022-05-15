from django import forms
from .models import Contacto, Marcas, Productos, Categorias
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ConctactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        widgets={
            'mensaje': forms.Textarea(attrs={
                'rows':5,
                'cols':30
                }),
        }
        fields = '__all__'


class ProductoForm(forms.ModelForm):

    class Meta:
        model = Productos
        fields = ["nombre", "marca", "descripcion", "precio", "stock", "categoria", "imagen","videoid","destacado"]
        

class CategoriaForm(forms.ModelForm):

    class Meta:
        model = Categorias
        fields = ["nombre"]
        

class MarcaForm(forms.ModelForm):
    
    class Meta:
        model = Marcas
        fields = ["nombre"]


class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ["username", "first_name","last_name","email","password1","password2"]
        
class CustomUserCreationFormListado(UserCreationForm):
    
    class Meta:
        model = User
        fields = ["username", "first_name","last_name","email","password1","password2"]
        