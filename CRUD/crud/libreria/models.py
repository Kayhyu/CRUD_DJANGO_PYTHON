from django.db import models

# Create your models here.

class libro(models.Model):
    id=models.AutoField(primary_key=True)
    titulo=models.CharField(max_length=100, verbose_name='Titulo')
    imagen=models.ImageField(upload_to="imagenes/",null=True,blank=True,verbose_name='Imagen')
    descripcion=models.TextField(verbose_name='Descripcion',null=True)
   
    def __str__(self): # se muestra en el formulario
       fila="Titulo: " + self.titulo + "-" + "Descripcion: " + self.descripcion
       return fila
   
    #borra imagen, total
    def delete(self,user=None, Keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()
