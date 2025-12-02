from django.contrib import admin
from .models import Proyecto  


class ProyectoAdmin(admin.ModelAdmin):
   
    list_display = ('titulo', 'url_demo', 'fecha_creacion')
    list_filter = ('fecha_creacion',)
    search_fields = ('titulo', 'descripcion')
    
admin.site.register(Proyecto, ProyectoAdmin)