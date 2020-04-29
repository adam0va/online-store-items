from django.db import models
import uuid


class Item(models.Model):
    DAIRY = 'DR'
    BAKERY = 'BK'
    FRUITS = 'FR'
    VEGETABLES = 'VG'
    BEVERAGES = 'BEV'
    OTHER = 'OTH'
    CATEGORY_CHOICES = [
        (DAIRY, 'Dairy'),
        (BAKERY, 'Bakery'),
        (FRUITS, 'Fruits'),
        (VEGETABLES, 'Vegetables'),
        (BEVERAGES, 'Beverages'),
        (OTHER, 'Other')
    ]

    name = models.CharField(max_length=200)
    amount = models.IntegerField(default=0, blank=False)
    category = models.CharField(choices=CATEGORY_CHOICES, default=OTHER, max_length=100)
    price = models.FloatField(default=0)
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to=f'items/images/', null=True, blank=True)

    def __str__(self):
        return f'{self.name} {self.amount} {self.category}, {self.price}, uuid: {self.uuid}'
