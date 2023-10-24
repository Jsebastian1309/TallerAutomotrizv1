from django.shortcuts import render,redirect
from django.contrib.auth.decorators import user_passes_test
from usuarios.models import Usuario
from usuarios.models import Arl
from usuarios.forms import UsuarioForm,UsuarioUpdateForm,ArlForm,ArlUpdateForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
 
@login_required
def usuario_crear(request):
    titulo="Usuario"
    if request.method== 'POST':
        form= UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'El usuario se creo correctamente.')
            return redirect('usuarios')
        else:
            messages.error(request, 'El formulario tiene errores.')
    else:
        form= UsuarioForm()
    context={
        "titulo":titulo,
        "form":form
        }
    return render(request,"usuarios/usuario/crear.html", context)

@login_required
def usuario_listar(request):
    titulo = "Usuarios"
    modulo = "Usuarios"
    usuarios = Usuario.objects.all()
    usuarios_cliente = usuarios.filter(tipo_usuario=Usuario.TipoUsuario.CLIENTE)
    otros_usuarios = usuarios.exclude(tipo_usuario=Usuario.TipoUsuario.CLIENTE)

    context = {
        "titulo": titulo,
        "modulo": modulo,
        "usuarios_cliente": usuarios_cliente,
        "otros_usuarios": otros_usuarios,
    }
    return render(request, "usuarios/usuario/listar.html", context)

@login_required
def usuario_modificar(request, pk):
    titulo = "Usuario"
    usuario = Usuario.objects.get(id=pk)

    if request.method == 'POST':
        form = UsuarioUpdateForm(request.POST, instance=usuario)

        if form.is_valid():
            new_username = form.cleaned_data.get('nombreusuario')
            if new_username != usuario.nombreusuario:
                if Usuario.objects.filter(nombreusuario=new_username).exclude(id=usuario.id).exists():
                    messages.error(request, 'El nombre de usuario ya está en uso. Por favor, elija otro.')
                    return render(request, "usuarios/usuario/modificar.html", {"titulo": titulo, "form": form})

            form.save()
            messages.success(request, 'El formulario se ha modificado correctamente.')
            return redirect('usuarios')
    else:
        form = UsuarioUpdateForm(instance=usuario)

    context = {
        "titulo": titulo,
        "form": form
    }
    return render(request, "usuarios/usuario/modificar.html", context)
def usuario_eliminar(request, pk):
    try:
        usuario = Usuario.objects.get(id=pk)
        try:
            user = User.objects.get(username=usuario.nombreusuario)
            user.delete()
        except User.DoesNotExist:
            pass  
        usuario.delete()
        
        messages.success(request, 'El usuario se eliminó correctamente.')
    except Usuario.DoesNotExist:
        messages.error(request, 'El usuario no existe.')

    return redirect('usuarios')

#views de tabla arl
@login_required
def arl_crear(request):
    titulo="Arl"
    if request.method== 'POST':
        form= ArlForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'El Arl se creo correctamente.')
            return redirect('arls')
        else:
            messages.error(request, 'El formulario tiene errores.')
    else:
        form= ArlForm()
    context={
        "titulo":titulo,
        "form":form
        }
    return render(request,"usuarios/arl/crear.html", context)

@login_required
def arl_listar(request):
    titulo="Arl"
    modulo ="Usuarios"
    arl= Arl.objects.all()
    context={
        "titulo":titulo,
        "modulo":modulo,
        "arls":arl
    }
    return render(request,"usuarios/arl/listar.html", context)

@login_required
def arl_modificar(request,pk):
    titulo="Arl"
    arl= Arl.objects.get(id=pk)
    if request.method== 'POST':
        form= ArlUpdateForm(request.POST, instance=arl)
        if form.is_valid():
            form.save()
            messages.success(request, 'El formulario se modifico correctamente.')
            return redirect('arls')
    else:
        form= ArlUpdateForm(instance=arl)
    context={
        "titulo":titulo,
        "form":form
        }
    return render(request,"usuarios/arl/modificar.html", context)

@login_required
def arl_eliminar(request,pk):
    arl = Arl.objects.filter(id=pk)
    arl.delete()
    return redirect('arls')

 