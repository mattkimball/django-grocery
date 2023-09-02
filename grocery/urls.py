from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include

index = lambda request: render(request, 'index.html')

urlpatterns = [
    path('', index, name='index'),
    path('items/', include('items.urls')),
    path('categories/', include('categories.urls')),
    path('admin/', admin.site.urls),
]