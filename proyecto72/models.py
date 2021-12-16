from django.db import models

# Create your models here.
class persona(models.model):
    id = models.autofield(primary_key=true)
    nombre= models.charfield(max_lenght=60)
    apellido= models.charfield(max_lenght=100)
    club= models.charfield(max_lenght=50)
    class Meta:
        verbose_name= ('Persona')
        verbose_name_plural= ('Personas')
        def __str__(self):
            return self.nombre
