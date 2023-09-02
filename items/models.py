from django.db import models
from simple_history.models import HistoricalRecords


class Item(models.Model):
    name = models.CharField(max_length=100, unique=True)
    history = HistoricalRecords()
    
    
    def __str__(self):
        return self.name
    
    
    @property
    def category_list(self):
        categoires = self.categories.all()
        if categoires.exists():
            return ', '.join([category.name for category in categoires])
        return 'None'
