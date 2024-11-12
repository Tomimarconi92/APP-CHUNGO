from django.db import models

class GustoHelado(models.Model):
    CATEGORIAS = [('CREMAS','CREMAS'),
                  ('CREMAS FRUTALES','CREMAS FRUTALES'),
                  ('CHOCOLATE','CHOCOLATE'),
                  ('DULCE DE LECHE','DULCE DE LECHE'),
                  ('FRUTALES','FRUTALES')
                ]

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='gustos/', blank=True, null=True)  # Almacenará las imágenes subidas
    categoria = models.CharField(max_length=50, choices=CATEGORIAS, default='crema')

    def __str__(self):
        return self.nombre