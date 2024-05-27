from django.db import models
# Create your models here.


class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)



class Recipe(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    prep_method = models.TextField()
    photo = models.URLField()
    ingredients = models.ManyToManyField(Ingredient)
    user = models.ForeignKey(to="users.CustomUser", on_delete=models.CASCADE,default=None)
    average_rating = models.DecimalField(max_digits=5, decimal_places=1, default=0)
    rated_by = models.IntegerField(default=0)
    all_rating = models.DecimalField(max_digits=15, decimal_places=1, default=0)








