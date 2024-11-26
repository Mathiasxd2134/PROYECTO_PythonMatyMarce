from django.db import models
from django.contrib.auth.models import User

class Reseña(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='imagenes_reseñas/', null=True, blank=True)  # Aquí agregamos el campo imagen

    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    reseña = models.ForeignKey('Reseña', on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)  # Este campo debería existir
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario de {self.autor.username} sobre {self.reseña.titulo}"