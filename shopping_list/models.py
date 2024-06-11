import uuid

from django.db import models



class ShoppingItem(models.Model):
    id = models.UUIDField(primary_key=True, default = uuid.uuid4)       # defining our own ID by using django's UUIDField to prevent people from easily accesing records
    name = models.CharField(max_length=100)
    purchased = models.BooleanField()

    def __str__(self):
        return f'{self.name}'
