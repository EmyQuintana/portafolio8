from django.db import models

class Proyecto(models.Model):
 
    titulo = models.CharField(max_length=100, verbose_name="Título del Proyecto")
    
  
    descripcion = models.TextField(verbose_name="Descripción (Problema Resuelto)")
    
  
    imagen = models.ImageField(
        upload_to='proyectos/', 
        verbose_name="Miniatura del Proyecto", 
        null=True, 
        blank=True
    )
    
   
    url_github = models.URLField(
        verbose_name="Enlace a GitHub/Repositorio", 
        blank=True
    )
    
 
    url_demo = models.URLField(
        verbose_name="Enlace a Demo en Vivo (Deploy)", 
        blank=True
    )
    
   
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Proyecto de Portafolio"
        verbose_name_plural = "Proyectos de Portafolio"
        ordering = ['-fecha_creacion']

    def __str__(self):
        """Devuelve el título del proyecto en el panel de administración."""
        return self.titulo