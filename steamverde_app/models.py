from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=45, null=False)
    def __str__(self):
        return self.nombre
    class Meta:
        app_label = 'steamverde_app'

class Pelicula(models.Model):
    titulo = models.CharField(max_length=200, null=False)
    sinopsis = models.TextField(max_length=2000, null=True)
    anio = models.IntegerField(null=False)
    actores = models.TextField(max_length=2000)
    duracion = models.IntegerField(null=False)
    def __str__(self):
        return self.titulo
    class Meta:
        app_label = 'steamverde_app'

class User(models.Model):
    username = models.CharField(max_length=45)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    admin = models.BooleanField(null=False, default=False)
    def __str__(self):
        return self.username
    class Meta:
        app_label = 'steamverde_app'

class Calificacion(models.Model):
    valor = models.IntegerField(null=False)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    pelicula = models.ForeignKey(Pelicula, on_delete=models.PROTECT)
    def __str__(self):
        return str(self.valor)+" Usuario:"+str(self.usuario)+" Pelicula:"+str(self.pelicula)
    class Meta:
        app_label = 'steamverde_app'

class PeliculaCategoria(models.Model):
    pelicula = models.ForeignKey(Pelicula, on_delete=models.PROTECT)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    def __str__(self):
        return str(self.pelicula)+" Cat: "+str(self.categoria)
    class Meta:
        app_label = 'steamverde_app'

class Comentario(models.Model):
    texto = models.TextField(max_length=2000, null=True)
    fechahora = models.DateTimeField()
    activo = models.BooleanField()
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    pelicula = models.ForeignKey(Pelicula, on_delete=models.PROTECT)
    def __str__(self):
        return str(self.texto)+" User:"+str(self.usuario)+" Peli:"+str(self.pelicula)
    class Meta:
        app_label = 'steamverde_app'
