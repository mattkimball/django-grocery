from django.shortcuts import render

from htmx_modal_forms.views import HTMXModalCreateView, HTMXModalUpdateView, HTMXModalDeleteView

from .forms import ItemForm
from .models import  Item


items_home = lambda request: render(request, 'items/index.html')

item = lambda request, pk: render(request, 'items/index.html#item', {'item': Item.objects.get(id=pk)})

item_list = lambda request: render(request, 'items/index.html#item-list', {'items': Item.objects.order_by('name')})


class ItemCreateView(HTMXModalCreateView):
    model = Item
    template_name = 'items/index.html#item-form'
    form_class = ItemForm


class ItemUpdateView(HTMXModalUpdateView):
    model = Item
    template_name = 'items/index.html#item-form'
    form_class = ItemForm


class ItemDeleteView(HTMXModalDeleteView):
    model = Item
    template_name = 'items/index.html#item-form'
