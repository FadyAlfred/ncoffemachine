import uuid

from django.db import models


class ProductTypes(models.TextChoices):
    LARGE = 'L', 'Large'
    SMALL = 'S', 'Small'
    ESPRESSO = 'E', 'Espresso'


class CoffeeMachine(models.Model):
    class Editions(models.TextChoices):
        BASE = 'B', 'Base'
        PREMIUM = 'P', 'Premium'
        DELUXE = 'D', 'Deluxe'

    id = models.AutoField(primary_key=True)
    sku = models.CharField(max_length=50)
    water_line_compatible = models.BooleanField()
    type = models.CharField(max_length=1, choices=ProductTypes.choices)
    edition = models.CharField(max_length=1, choices=Editions.choices)


class CoffeePod(models.Model):
    class Sizes(models.IntegerChoices):
        ONE = 1, 'One'
        THREE = 3, 'Three'
        FIVE = 5, 'Five'
        SEVEN = 7, 'Seven'

    class Flavors(models.TextChoices):
        VANILLA = 'V', 'Vanilla'
        CARAMEL = 'C', 'Carmel'
        PSL = 'P', 'Psl'
        MOCHA = 'M', 'Mocha'
        HAZELNUT = 'H', 'Hazelnut'

    id = models.AutoField(primary_key=True)
    sku = models.CharField(max_length=50)
    size = models.IntegerField(choices=Sizes.choices)
    type = models.CharField(max_length=1, choices=ProductTypes.choices)
    flavor = models.CharField(max_length=1, choices=Flavors.choices)

