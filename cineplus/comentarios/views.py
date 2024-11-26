from django.shortcuts import render, get_object_or_404, redirect
from .models import Reseña, Comentario
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ComentarioForm, ReseñaForm
from .forms import ComentarioForm, ReseñaForm




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

@login_required
def crear_reseña(request):
    if request.method == 'POST':
        # Obtener datos del formulario
        titulo = request.POST.get('titulo')
        descripcion = request.POST.get('descripcion')
        imagen = request.FILES.get('imagen')  # Obtener la imagen del formulario
        
        # Crear una nueva reseña
        reseña = Reseña.objects.create(
            titulo=titulo,
            descripcion=descripcion,
            autor=request.user,
            imagen=imagen  # Guardar la imagen en la reseña
        )
        
        # Redirigir a la lista de reseñas después de crearla
        return redirect('lista_reseñas')
    
    return render(request, 'comentarios/crear_reseña.html')

@login_required
def agregar_comentario(request, reseña_id):
    reseña = get_object_or_404(Reseña, pk=reseña_id)
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.reseña = reseña
            comentario.autor = request.user
            comentario.save()
            return HttpResponseRedirect(reverse('detalle_reseña', args=[reseña_id]))
    else:
        form = ComentarioForm()
    return render(request, 'comentarios/agregar_comentario.html', {'reseña': reseña, 'form': form})



@login_required
def lista_reseñas(request):
    reseñas = Reseña.objects.all()  # Obtenemos todas las reseñas
    reseña_form = ReseñaForm()  # Formulario para crear reseñas
    comentario_form = ComentarioForm()  # Formulario para agregar comentarios

    if request.method == 'POST':
        # Si se envió el formulario de creación de reseñas
        if 'crear_reseña' in request.POST:
            reseña_form = ReseñaForm(request.POST)
            if reseña_form.is_valid():
                nueva_reseña = reseña_form.save(commit=False)
                nueva_reseña.autor = request.user  # Asocia la reseña al usuario autenticado
                nueva_reseña.save()
                return HttpResponseRedirect(reverse('lista_reseñas'))

        # Si se envió el formulario de agregar comentarios
        if 'crear_comentario' in request.POST:
            comentario_form = ComentarioForm(request.POST)
            reseña_id = request.POST.get('reseña_id')  # Capturamos el ID de la reseña
            reseña = get_object_or_404(Reseña, id=reseña_id)  # Obtenemos la reseña
            if comentario_form.is_valid():
                nuevo_comentario = comentario_form.save(commit=False)
                nuevo_comentario.reseña = reseña
                nuevo_comentario.autor = request.user
                nuevo_comentario.save()
                return HttpResponseRedirect(reverse('lista_reseñas'))

    return render(request, 'comentarios/lista_reseñas.html', {
        'reseñas': reseñas,
        'reseña_form': reseña_form,
        'comentario_form': comentario_form,
    })