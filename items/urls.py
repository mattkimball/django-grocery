from django.urls import path
from . import views


app_name = 'items'

urlpatterns = [
    path('', views.items_home, name='home'),
    path('new', views.ItemCreateView.as_view(), name='create'),
    path('item-list', views.item_list, name='item-list'),
    path('<int:pk>', views.item, name='item'),
    path('<int:pk>/update', views.ItemUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', views.ItemDeleteView.as_view(), name='delete'),
]