from django.db import models

# Create your models here.

class User(models.Model):
    Name = models.CharField(max_length=100, blank=False, null=False)
    Apellido = models.CharField(max_length=100, blank=False, null=False)
    Nickname = models.CharField(max_length=50, blank=False, null=False, unique=True)
    Correo = models.EmailField(unique=True)

    def __str__(self):
        return self.Nickname

class Categoria(models.Model):
    Categoria = models.CharField(max_length=50, blank=False, null=False, unique=True)

    def __str__(self):
        return self.Categoria

class Periodo(models.Model):
    No_Periodo = models.IntegerField(unique=True,blank=False, null=False)

    def __str__(self):
        return str(self.No_Periodo)

class Grupo(models.Model):
    No_Grupo = models.IntegerField(unique=True,blank=False, null=False)

    def __str__(self):
        return str(self.No_Grupo)

class Elemento(models.Model):
    Nombre = models.CharField(max_length=50,blank=False, null=False, unique=True)
    Simbolo = models.CharField(max_length=3, blank=False, null=False, unique=True)
    No_Atomico = models.IntegerField(blank=False, null=False, unique=True)
    Periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE, blank=False, null=False)
    Grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, blank=False, null=False)
    Masa_Atomica = models.FloatField(blank=False, null=False)
    Densidad = models.FloatField(blank=False, null=False)
    Categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, blank=False, null=False)
    Creado_por = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    Informacion = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.Nombre