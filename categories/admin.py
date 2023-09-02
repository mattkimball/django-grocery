from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from .models import Category


admin.site.register(Category, SimpleHistoryAdmin)
