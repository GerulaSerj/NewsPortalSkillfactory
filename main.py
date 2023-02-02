from django.db import models


class Product(models.Model):
    name = models.CharField(max_length = 255)
    price = models.FloatField(default = 0.0)

class Staff(models.Model):
    full_name = models.CharField(max_length = 255)
    position = models.CharField(max_length = 255)
    labor_contract = models.IntegerField()

director = 'DI'
admin = 'AD'
cook = 'CO'
cashier = 'CA'
cleaner = 'CL'

POSITIONS = [
    (director, 'Директор'),
    (admin, 'Администратор'),
    (cook, 'Повар'),
    (cashier, 'Кассир'),
    (cleaner, 'Уборщик')
]

position = models.CharField(max_length = 2,
                            choices = POSITIONS,
                            default = cashier)

