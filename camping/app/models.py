from django.db import models

class Usuarios(models.Model):
    ''''
        Este modelo esta enfocado en la creacion de usuario el cual contiene campos adicciones a los genericos.
        Fecha de creacion: 1/12/2021
        autores: Stiven Restrepo, Santiago Hernandez
    '''
    sexos = (
        ('Femenino', 'femenino'), 
        ('Masculino', 'masculino'),
        ('Otro', 'otro'), 
        ('No definido', 'no_definido'),  
    )
    sexo = models.CharField(max_length=20, blank=False, null=False, choices=sexos)
    id = models.AutoField(primary_key= True)
    nombre_completo = models.CharField('Nombre completo', max_length=30, blank=False, null=False)
    state = models.BooleanField('Usuario Activado/Usuario no Activado', default=True)
    fecha_usuario = models.DateField('Fecha de Creacion', auto_now=False, auto_now_add=True)
    telefono = models.IntegerField('Telefono', blank=False, null=False)


    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return self.nombre_completo


class Publicaciones(models.Model):
    id = models.AutoField(primary_key= True)
    nombre_lugar = models.CharField(max_length=120, blank=False, null=False)
    ubicacion = models.CharField(max_length=250, blank=False, null=False)
    fotos = models.ImageField(upload_to='documents/wild-life-v1/app/static/images/')
    videos = models.FileField(upload_to='documents/wild-life-v1/app/static/videos/')
    descripcion = models.CharField(max_length=250, blank=False, null=False)
    fecha_publicacion = models.DateField('Fecha de publicacion', auto_now=False, auto_now_add=True)
    nombre_guia = models.CharField('Guia',max_length=120, blank=False, null=False)
    nombre_usuario = models.ForeignKey(Usuarios, on_delete = models.CASCADE)


    class Meta:
        verbose_name = 'Publicacion'
        verbose_name_plural = 'Publicaciones'

    def __str__(self):
        return self.nombre_lugar