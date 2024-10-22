from django.db import models

class Crud(models.Model):
    Nom_Product =models.CharField(max_length=200)

##para mirarl la descripcion del producto en el admin 
    def __str__(self):
        return self.Nom_Product
