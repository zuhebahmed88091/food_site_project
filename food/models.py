from email.policy import default
from django.db import models

# Create your models here.


class Item(models.Model):
    item_name = models.CharField(max_length=200)
    item_description = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500, default="https://assets.materialup.com/uploads/b03b23aa-aa69-4657-aa5e-fa5fef2c76e8/preview.png")

    def __str__(self):
        return self.item_name
