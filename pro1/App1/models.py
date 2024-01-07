from django.db import models

# Create your models here.
class Item(models.Model):
    item_text = models.CharField(max_length=200)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.item_text
