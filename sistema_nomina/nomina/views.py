from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Departamento, Permiso, TipoContrato, Empleado, Rol, Cargo, TipoPermiso
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import CargoForm, DepartamentoForm, TipoContratoForm, EmpleadoForm, RolForm, PermisoForm, TipoPermisoForm

# Create your views here.


def home(request):
    data = {
        'title': 'Sistema de Nómina',
        'description': 'Gestión de empleados y pagos',
        'author': 'Naomi ',
        'year': 2025,
    }
    return render(request, 'home.html', data)

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'User already exists'
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'error': 'Password do not match'
        })


def home1(request):
    return render(request, 'home1.html')


def singout(request):
    logout(request)
    return redirect('home1')


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Username or password is incorrect'
            })
        else:
            login(request, user)
            return redirect('home')


# VISTAS---------------------------------

def cargo_list(request):
    cargos = Cargo.objects.all()
    query = request.GET.get('q', None)
    if query:
        cargos = Cargo.objects.filter(descripcion__icontains=query)
    context = {'cargos': cargos, 'title': 'Listado de Cargos'}
    return render(request, 'cargo/cargo_list.html', context)


def cargo_create(request):
    context = {'title': 'Ingresar Cargo'}
    if request.method == "GET":
        form = CargoForm()
        context['form'] = form
        return render(request, 'cargo/cargo_create.html', context)
    else:
        form = CargoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nomina:cargo_list')
        else:
            context['form'] = form
            return render(request, 'cargo/cargo_create.html', context)


def cargo_update(request, id):
    context = {'title': 'Actualizar Cargo'}
    cargo = get_object_or_404(Cargo, pk=id)
    if request.method == 'GET':
        form = CargoForm(instance=cargo)
        context['form'] = form
        return render(request, 'cargo/cargo_create.html', context)
    else:
        form = CargoForm(request.POST, instance=cargo)
        if form.is_valid():
            form.save()
            return redirect('nomina:cargo_list')
        else:
            context['form'] = form
            return render(request, 'cargo/cargo_create.html', context)


def cargo_delete(request, id):
    cargo = get_object_or_404(Cargo, pk=id)
    if request.method == "GET":
        context = {'title': 'Eliminar Cargo', 'cargo': cargo, 'error': ''}
        return render(request, 'cargo/cargo_delete.html', context)
    else:
        cargo.delete()
        return redirect('nomina:cargo_list')

# DEPARTAMENTOOOOOOOOOOOOOOOO-------------


def departamento_list(request):
    departamentos = Departamento.objects.all()
    query = request.GET.get('q', None)
    if query:
        departamentos = Departamento.objects.filter(
            descripcion__icontains=query)
    context = {'departamentos': departamentos,
               'title': 'Listado de Departamentos'}
    return render(request, 'departamento/departamento_list.html', context)


def departamento_create(request):
    context = {'title': 'Ingresar Departamento'}

    if request.method == "GET":
        form = DepartamentoForm()
        context['form'] = form
        return render(request, 'departamento/departamento_create.html', context)

    else:
        form = DepartamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nomina:departamento_list')
        else:
            context['form'] = form
            return render(request, 'departamento/departamento_create.html', context)


def departamento_update(request, id):
    context = {'title': 'Actualizar Departamento'}
    departamento = get_object_or_404(Departamento, pk=id)
    if request.method == 'GET':
        form = DepartamentoForm(instance=departamento)
        context['form'] = form
        return render(request, 'departamento/departamento_create.html', context)
    else:
        form = DepartamentoForm(request.POST, instance=departamento)
        if form.is_valid():
            form.save()
            return redirect('nomina:departamento_list')
        else:
            context['form'] = form
            return render(request, 'departamento/departamento_create.html', context)


def departamento_delete(request, id):
    departamento = get_object_or_404(Departamento, pk=id)
    if request.method == "GET":
        context = {'title': 'Eliminar Departamento',
                   'departamento': departamento, 'error': ''}
        return render(request, 'departamento/departamento_delete.html', context)
    else:
        departamento.delete()
        return redirect('nomina:departamento_list')

# TIPO CONTRATO


def tipocontrato_list(request):
    contratos = TipoContrato.objects.all()
    query = request.GET.get('q', None)
    if query:
        contratos = TipoContrato.objects.filter(descripcion__icontains=query)
    context = {'contratos': contratos, 'title': 'Listado de Tipos de Contrato'}
    return render(request, 'tipocontrato/tipocontrato_list.html', context)


def tipocontrato_create(request):
    context = {'title': 'Ingresar Tipo de Contrato'}
    if request.method == "GET":
        form = TipoContratoForm()
        context['form'] = form
        return render(request, 'tipocontrato/tipocontrato_create.html', context)
    else:
        form = TipoContratoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nomina:tipocontrato_list')
        else:
            context['form'] = form
            return render(request, 'tipocontrato/tipocontrato_create.html', context)


def tipocontrato_update(request, id):
    context = {'title': 'Actualizar Tipo de Contrato'}
    contrato = get_object_or_404(TipoContrato, pk=id)
    if request.method == 'GET':
        form = TipoContratoForm(instance=contrato)
        context['form'] = form
        return render(request, 'tipocontrato/tipocontrato_create.html', context)
    else:
        form = TipoContratoForm(request.POST, instance=contrato)
        if form.is_valid():
            form.save()
            return redirect('nomina:tipocontrato_list')
        else:
            context['form'] = form
            return render(request, 'tipocontrato/tipocontrato_create.html', context)


def tipocontrato_delete(request, id):
    contrato = get_object_or_404(TipoContrato, pk=id)
    if request.method == "GET":
        context = {'title': 'Eliminar Tipo de Contrato', 'contrato': contrato}
        return render(request, 'tipocontrato/tipocontrato_delete.html', context)
    else:
        contrato.delete()
        return redirect('nomina:tipocontrato_list')

    # EMPLEADOOOOOOOOOOOOOOOOO

def empleado_list(request):
    empleados = Empleado.objects.all()
    query = request.GET.get('q', None)
    if query:
        empleados = Empleado.objects.filter(nombre__icontains=query)
    context = {'empleados': empleados, 'title': 'Listado de Empleados'}
    return render(request, 'empleado/empleado_list.html', context)


def empleado_create(request):
    context = {'title': 'Registrar Empleado'}
    if request.method == "GET":
        form = EmpleadoForm()
        context['form'] = form
        return render(request, 'empleado/empleado_create.html', context)
    else:
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nomina:empleado_list')
        else:
            context['form'] = form
            return render(request, 'empleado/empleado_create.html', context)


def empleado_update(request, id):
    context = {'title': 'Actualizar Empleado'}
    empleado = get_object_or_404(Empleado, pk=id)
    if request.method == 'GET':
        form = EmpleadoForm(instance=empleado)
        context['form'] = form
        return render(request, 'empleado/empleado_create.html', context)
    else:
        form = EmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            return redirect('nomina:empleado_list')
        else:
            context['form'] = form
            return render(request, 'empleado/empleado_create.html', context)


def empleado_delete(request, id):
    empleado = get_object_or_404(Empleado, pk=id)
    if request.method == "GET":
        context = {'title': 'Eliminar Empleado', 'empleado': empleado}
        return render(request, 'empleado/empleado_delete.html', context)
    else:
        empleado.delete()
        return redirect('nomina:empleado_list')


#vIVASTAAAAAASSSSSSSSSSSSSSS DE ROLLL

def rol_list(request):
    roles = Rol.objects.all()
    query = request.GET.get('q')
    if query:
        roles = Rol.objects.filter(empleado__nombre__icontains=query)  # Búsqueda por nombre de empleado
    context = {
        'roles': roles,
        'title': 'Listado de Roles'
    }
    return render(request, 'rol/rol_list.html', context)

def rol_create(request):
    context = {'title': 'Crear Rol'}
    if request.method == 'GET':
        form = RolForm()
        context['form'] = form
        return render(request, 'rol/rol_create.html', context)
    else:
        form = RolForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nomina:rol_list')
        else:
            context['form'] = form
            return render(request, 'rol/rol_create.html', context)

def rol_update(request, id):
    rol = get_object_or_404(Rol, pk=id)
    context = {'title': 'Actualizar Rol'}
    if request.method == 'GET':
        form = RolForm(instance=rol)
        context['form'] = form
        return render(request, 'rol/rol_create.html', context)
    else:
        form = RolForm(request.POST, instance=rol)
        if form.is_valid():
            form.save()
            return redirect('nomina:rol_list')
        else:
            context['form'] = form
            return render(request, 'rol/rol_create.html', context)

def rol_delete(request, id):
    rol = get_object_or_404(Rol, pk=id)
    if request.method == 'GET':
        return render(request, 'rol/rol_delete.html', {'rol': rol, 'title': 'Eliminar Rol'})
    else:
        rol.delete()
        return redirect('nomina:rol_list')
    
#vIVASTAAAAAASSSSSSSSSSSSSSS DE PERMISOOO

def permiso_list(request):
    permisos = Permiso.objects.all()
    query = request.GET.get('q')
    if query:
        permisos = Permiso.objects.filter(empleado__nombre__icontains=query)  # Búsqueda por nombre de empleado
    context = {
        'permisos': permisos,
        'title': 'Listado de Permisos'
    }
    return render(request, 'permiso/permiso_list.html', context)

def permiso_create(request):
    context = {'title': 'Crear Permiso'}
    if request.method == 'GET':
        form = PermisoForm()
        context['form'] = form
        return render(request, 'permiso/permiso_create.html', context)
    else:
        form = PermisoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nomina:permiso_list')
        else:
            context['form'] = form
            return render(request, 'permiso/permiso_create.html', context)

def permiso_update(request, id):
    permiso = get_object_or_404(Permiso, pk=id)
    context = {'title': 'Actualizar Permiso'}
    if request.method == 'GET':
        form = PermisoForm(instance=Permiso)
        context['form'] = form
        return render(request, 'permiso/permiso_create.html', context)
    else:
        form = PermisoForm(request.POST, instance=Permiso)
        if form.is_valid():
            form.save()
            return redirect('nomina:permiso_list')
        else:
            context['form'] = form
            return render(request, 'permiso/permiso_create.html', context)

def permiso_delete(request, id):
    permiso = get_object_or_404(Permiso, pk=id)
    if request.method == 'GET':
        return render(request, 'permiso/permiso_delete.html', {'permiso': permiso, 'title': 'Eliminar Permiso'})
    else:
        permiso.delete()
        return redirect('nomina:permiso_list')

#Vista de tipo de permisos

def tipopermiso_list(request):
    permisos = TipoPermiso.objects.all()
    query = request.GET.get('q', None)
    if query:
        permisos = TipoPermiso.objects.filter(descripcion__icontains=query)
    context = {'permisos': permisos, 'title': 'Listado de Tipos de Permiso'}
    return render(request, 'tipopermiso/tipopermiso_list.html', context)


def tipopermiso_create(request):
    context = {'title': 'Ingresar Tipo de Permiso'}
    if request.method == "GET":
        form = TipoPermisoForm()
        context['form'] = form
        return render(request, 'tipopermiso/tipopermiso_create.html', context)
    else:
        form = TipoPermisoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nomina:tipopermiso_list')
        else:
            context['form'] = form
            return render(request, 'tipopermiso/tipopermiso_create.html', context)


def tipopermiso_update(request, id):
    context = {'title': 'Actualizar Tipo de Contrato'}
    permiso = get_object_or_404(TipoPermiso, pk=id)
    if request.method == 'GET':
        form = TipoPermisoForm(instance=permiso)
        context['form'] = form
        return render(request, 'tipopermiso/tipopermiso_create.html', context)
    else:
        form = TipoPermisoForm(request.POST, instance=permiso)
        if form.is_valid():
            form.save()
            return redirect('nomina:tipopermiso_list')
        else:
            context['form'] = form
            return render(request, 'tipopermiso/tipopermiso_create.html', context)


def tipopermiso_delete(request, id):
    permiso = get_object_or_404(TipoPermiso, pk=id)
    if request.method == "GET":
        context = {'title': 'Eliminar Tipo de Permiso', 'permiso': permiso}
        return render(request, 'tipopermiso/tipopermiso_delete.html', context)
    else:
        permiso.delete()
        return redirect('nomina:tipopermiso_list')
