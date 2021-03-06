from django.db import models
import uuid


class Item(models.Model):
    #помада тушь тон пудра румяна подводка
    LIPSTICK = 'Lipstick'
    MASCARA = 'Mascara'
    FOUNDATION = 'Foundation'
    POWDER = 'Powder'
    BLUSH = 'Blush'
    EYELINER = 'Eyeliner'
    ITEM_CATEGORY = [
        (LIPSTICK, 'Lipstick'),
        (MASCARA, 'Mascara'),
        (FOUNDATION, 'Foundation'),
        (POWDER, 'Powder'),
        (BLUSH, 'Blush'),
        (EYELINER, 'Eyeliner')
    ]

    name = models.CharField(max_length=200)
    amount = models.IntegerField(default=0, blank=False)
    category = models.CharField(choices=ITEM_CATEGORY, default=LIPSTICK, max_length=100)
    brand = models.CharField(max_length=100, null=True)
    color = models.CharField(max_length=50, null=True)
    price = models.FloatField(default=0)
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.CharField(max_length=150, null=True)

    def __str__(self):
        return f'{self.name} {self.amount} {self.category}, {self.price}, uuid: {self.uuid}, brand: {self.brand}, ' \
               f'color: {self.color}'
