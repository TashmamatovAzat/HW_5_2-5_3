from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    firm = models.ForeignKey('Firm', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.price} {self.firm.name} {self.category.name}'


class Firm(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name} по адресу {self.address}'


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
