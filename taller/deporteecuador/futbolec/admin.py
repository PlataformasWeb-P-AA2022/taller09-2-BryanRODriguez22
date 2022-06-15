# from msilib.schema import Class
from django.contrib import admin

# Register your models here.
from futbolec.models import Equipo,Jugador,Campeonato,CampeonatoEquipo

admin.site.register(Equipo)

class JugadorAdmin(admin.ModelAdmin):
    list_display = ('nombre' , 'posicion','numero','sueldo','equipofut')
    search_fields = ('nombre',)
admin.site.register(Jugador, JugadorAdmin)

admin.site.register(Campeonato)

class CampeonatoEquipoAdmin(admin.ModelAdmin):
    list_display = ('anio','equipo_de_fut','campeonato')
    search_fields = ('equipo_de_fut__nombre', 'campeonato__nombre')
admin.site.register(CampeonatoEquipo,CampeonatoEquipoAdmin)