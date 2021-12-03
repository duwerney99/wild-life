from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class UsuariosResource(resources.ModelResource):
    class Meta:
        model = Usuarios


class UsuariosAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre_completo']
    list_display = ('nombre_completo', 'state', 'fecha_usuario')
    resources_class = UsuariosResource


class PublicacionesResource(resources.ModelResource):
    class Meta:
        model = Publicaciones



class PublicacionesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre_lugar']
    list_display = ('id','nombre_lugar', 'nombre_guia', 'fecha_publicacion')
    resources_class = PublicacionesResource

admin.site.register(Usuarios, UsuariosAdmin)
admin.site.register(Publicaciones, PublicacionesAdmin)