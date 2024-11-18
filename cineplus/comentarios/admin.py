from django.contrib import admin

# Register your models here.

from .models import Reseña,Comentario

admin.site.register(Reseña)
admin.site.register(Comentario)
