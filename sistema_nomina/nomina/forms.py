from django import forms
from .models import Cargo, Departamento, TipoContrato, Empleado, Rol, Permiso, TipoPermiso

# Formulario para el modelo Cargo
class CargoForm(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = ['descripcion']

# Formulario para el modelo Departamento
class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ['descripcion']

# Formulario para el modelo TipoContrato
class TipoContratoForm(forms.ModelForm):
    class Meta:
        model = TipoContrato
        fields = ['descripcion']

# Formulario para el modelo Empleado
class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre', 'cedula', 'direccion', 'sexo', 'sueldo', 'cargo', 'departamento', 'tipo_contrato']

# Formulario para el modelo Rol
from django import forms
from .models import Rol

class RolForm(forms.ModelForm):
    class Meta:
        model = Rol
        fields = ['empleado', 'aniomes', 'sueldo', 'horas_extra', 'bono']

        # Es posible que desees excluir los campos que calculas en el modelo, ya que se calculan en el método save().
        # Para ello, podrías agregar algo como:
        # exclude = ['tot_ing', 'tot_des', 'neto']

class PermisoForm(forms.ModelForm):
    class Meta:
        model = Permiso
        fields = ['empleado', 'fecha_permiso', 'tipo_permiso', 'dias', 'horas','is_active']

class TipoPermisoForm(forms.ModelForm):
    class Meta:
        model = TipoPermiso
        fields = ['descripcion', 'frecuencia_dias']
