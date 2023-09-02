from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from .models import Item


admin.site.register(Item, SimpleHistoryAdmin)
