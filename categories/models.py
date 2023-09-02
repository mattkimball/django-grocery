from django.db import models

from simple_history.models import HistoricalRecords

from items.models import Item


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    items = models.ManyToManyField(Item, related_name='categories', blank=True)
    history = HistoricalRecords()
    
    
    def __str__(self):
        return self.name

    
    @property
    def item_list(self):
        if self.items.exists():
            return ', '.join([item.name for item in self.items.order_by('name')])
        return 'None'
