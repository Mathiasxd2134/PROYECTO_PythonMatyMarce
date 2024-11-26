from django import forms
from .models import Comentario, Reseña

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']

from django import forms
from .models import Reseña

class ReseñaForm(forms.ModelForm):
    class Meta:
        model = Reseña
        fields = ['titulo', 'descripcion', 'autor', 'imagen']  # Incluye 'imagen' en los campos