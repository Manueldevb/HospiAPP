from django.contrib import admin

# Register your models here.
# from .models.persona import Persona
from .models.paciente import Paciente
from .models.medico import Medico
from .models.familiarDesignado import FamiliarDesignado
from .models.signoVital import SignoVital
# admin.site.register(Persona)  
admin.site.register(Paciente)  
admin.site.register(Medico)
admin.site.register(FamiliarDesignado)
admin.site.register(SignoVital)
