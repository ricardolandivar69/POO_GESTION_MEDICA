from django.urls import path
from nomina.views import home, cargo_create,cargo_delete, cargo_list,cargo_update, departamento_create, departamento_delete,departamento_list, departamento_update, permiso_create, permiso_delete, permiso_list, permiso_update, tipocontrato_create, tipocontrato_delete, tipocontrato_list, tipocontrato_update, empleado_create, empleado_delete, empleado_list,empleado_update, rol_create, rol_delete, rol_list ,rol_update, tipopermiso_create, tipopermiso_delete, tipopermiso_list, tipopermiso_update
app_name = 'core'

urlpatterns = [
    path('', home, name='home'),
    path('cargos/', cargo_list, name='cargo_list'),
    path('cargos/nuevo/', cargo_create, name='cargo_create'),
    path('cargos/editar/<int:id>/', cargo_update, name='cargo_update'),
    path('cargos/eliminar/<int:id>/', cargo_delete, name='cargo_delete'),
    #deaprtamento
    path('departamento/', departamento_list, name='departamento_list'),
    path('departamento/crear/', departamento_create, name='departamento_create'),
    path('departamento/actualizar/<int:id>/', departamento_update, name='departamento_update'),
    path('departamento/eliminar/<int:id>/', departamento_delete, name='departamento_delete'),
    #tipo de contrato
    path('tipocontrato/', tipocontrato_list, name='tipocontrato_list'),
    path('tipocontrato/crear/',tipocontrato_create, name='tipocontrato_create'),
    path('tipocontrato/actualizar/<int:id>/', tipocontrato_update, name='tipocontrato_update'),
    path('tipocontrato/eliminar/<int:id>/', tipocontrato_delete, name='tipocontrato_delete'),
    #empleados
    path('empleado/', empleado_list, name='empleado_list'),
    path('empleado/crear/', empleado_create, name='empleado_create'),
    path('empleado/actualizar/<int:id>/', empleado_update, name='empleado_update'),
    path('empleado/eliminar/<int:id>/', empleado_delete, name='empleado_delete'),
    #ROL RUTAS 
    path('rol/', rol_list, name='rol_list'),
    path('rol/create/', rol_create, name='rol_create'),
    path('rol/<int:id>/update/', rol_update, name='rol_update'),
    path('rol/<int:id>/delete/', rol_delete, name='rol_delete'),
    #PERMISO
    path('permiso/', permiso_list, name='permiso_list'),
    path('permiso/create/', permiso_create, name='permiso_create'),
    path('permiso/<int:id>/update/', permiso_update, name='permiso_update'),
    path('permiso/<int:id>/delete/', permiso_delete, name='permiso_delete'),
    #TIPO PERMISO
    path('tipopermiso/', tipopermiso_list, name='tipopermiso_list'),
    path('tipopermiso/create/', tipopermiso_create, name='tipopermiso_create'),
    path('tipopermiso/<int:id>/update/', tipopermiso_update, name='tipopermiso_update'),
    path('tipopermiso/<int:id>/delete/', tipopermiso_delete, name='tipopermiso_delete'),
]