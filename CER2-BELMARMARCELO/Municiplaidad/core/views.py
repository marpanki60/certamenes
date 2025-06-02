from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import RegistroUsuarioForm,LoginForm,ObjetosReciclableForm
from .models import ObjetosReciclable
from django.db.models import Sum, Count

def primeraVista(request):
    totalobjetos = ObjetosReciclable.objects.count()
    sumacantidades = ObjetosReciclable.objects.aggregate(Sum('cantidadMaterial'))['cantidadMaterial__sum'] or 0

    context = {
        'totalobjetos': totalobjetos,
        'sumacantidades': sumacantidades,
    }
    return render(request, 'primeraVista.html', context)

def contactos(request):
    return render(request,"contactos.html")


def user_Login(request):
    if request.method=='POST':
        form= LoginForm(request.POST)
        if form.is_valid():
            cd= form.cleaned_data
            user= authenticate(request,
                                username = cd['username'],
                                password = cd['password'])
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return HttpResponse('Usuario auntenticado')
                else:
                    return HttpResponse('Usuario no esta activo')
            else:
                return HttpResponse('La informacion no es correcta')
    else:
        form= LoginForm()
        return render(request, 'login.html',{'form': form})

def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect('primeraVista')  
    else:
        form = RegistroUsuarioForm()
    return render(request, 'registration/registration.html', {'form': form})




@login_required
def agregar_objeto(request):
    if request.method == 'POST':
        form = ObjetosReciclableForm(request.POST)
        if form.is_valid():
            objeto = form.save(commit=False)
            objeto.usuario = request.user
            objeto.save()
            return redirect('historial_objetos')
    else:
        form = ObjetosReciclableForm()
    return render(request, 'agregar_objeto.html', {'form': form})

@login_required
def historial_objetos(request):
    objetos = ObjetosReciclable.objects.filter(usuario=request.user).order_by('-fechaCreacion')
    return render(request, 'historial_objetos.html', {'objetos': objetos})