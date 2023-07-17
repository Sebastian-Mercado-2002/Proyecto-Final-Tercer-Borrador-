from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from apps.posts.models import Post, Categoria

def index(request):
    return render(request, 'index.html')

def aplicacion_de_la_ia(request):
    try:
        categoria = Categoria.objects.get(nombre='Aplicación de la IA')
        posts = Post.objects.filter(categoria=categoria)
    except Categoria.DoesNotExist:
        posts = []
    return render(request, 'aplicacion_de_la_ia.html', {'posts': posts})

def impacto_educacion(request):
    try:
        categoria = Categoria.objects.get(nombre='Impacto de la IA en la Educación')
        posts = Post.objects.filter(categoria=categoria)
    except Categoria.DoesNotExist:
        posts = []
    return render(request, 'impacto_educacion.html', {'posts': posts})

def impacto_laboral(request):
    try:
        categoria = Categoria.objects.get(nombre='Impacto en el Mundo Laboral')
        posts = Post.objects.filter(categoria=categoria)
    except Categoria.DoesNotExist:
        posts = []
    return render(request, 'impacto_laboral.html', {'posts': posts})

def acerca_de(request):
    return render(request, 'acerca_de.html')

def contacto(request):
    return render(request, 'contacto.html')

def inicio(request):
    return render(request, 'inicio.html') 

def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.activo = True
            post.save()
            return redirect('index')  
    else:
        form = PostForm()
    return render(request, 'crear_post.html', {'form': form})

def aplicacion_de_la_ia(request):
    try:
        categoria = Categoria.objects.get(nombre='Aplicación de la IA')
        posts = Post.objects.filter(categoria=categoria)
    except Categoria.DoesNotExist:
        posts = []
    return render(request, 'aplicacion_de_la_ia.html', {'posts': posts, 'categoria': categoria})

def impacto_educacion(request):
    try:
        categoria = Categoria.objects.get(nombre='Impacto de la IA en educación')
        posts = Post.objects.filter(categoria=categoria)
    except Categoria.DoesNotExist:
        posts = []
    return render(request, 'impacto_educacion.html', {'posts': posts, 'categoria': categoria})

def impacto_laboral(request):
    try:
        categoria = Categoria.objects.get(nombre='Impacto en el mundo laboral')
        posts = Post.objects.filter(categoria=categoria)
    except Categoria.DoesNotExist:
        posts = []
    return render(request, 'impacto_laboral.html', {'posts': posts, 'categoria': categoria})

