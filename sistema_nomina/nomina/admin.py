from django.contrib import admin
from .models import Cargo, Departamento, Permiso, TipoContrato, Empleado, Rol, TipoPermiso

admin.site.register(Cargo)
admin.site.register(Departamento)
admin.site.register(TipoContrato)
admin.site.register(Empleado)
admin.site.register(Rol)
admin.site.register(Permiso)
admin.site.register(TipoPermiso)
