from django.db import models


class Prod(models.Model):
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=20)
    product = models.CharField(max_length=25)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField()

    photo = models.ImageField(upload_to='photo/%y/%m/%d/',blank=True)

    def __str__(self):
        return self.name
