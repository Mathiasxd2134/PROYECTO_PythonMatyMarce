from django.shortcuts import render, get_object_or_404
from .models import Reseña, Comentario
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse

def lista_reseñas(request):
    reseñas = Reseña.objects.all()
    return render(request, 'comentarios/lista_reseñas.html', {'reseñas': reseñas})

def detalle_reseña(request, reseña_id):
    reseña = get_object_or_404(Reseña, pk=reseña_id)
    comentarios = reseña.comentarios.all()
    return render(request, 'comentarios/detalle_reseña.html',{'reseña': reseña, 'comentarios': comentarios})

@login_required
def agregar_comentario(request, reseña_id):
    reseña = get_object_or_404(Reseña, pk=reseña_id)
    if request.method == 'POST':
        texto = request.POST.get('texto')
        comentario = Comentario(reseña=reseña, autor=request.user, texto=texto)
        comentario.save()
        return HttpResponseRedirect(reverse('detalle_reseña', args=[reseña_id]))
    return render(request, 'comentarios/agregar_comentario.html', {'reseña': reseña})