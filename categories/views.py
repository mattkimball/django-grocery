from django.shortcuts import render

from htmx_modal_forms.views import HTMXModalCreateView, HTMXModalUpdateView, HTMXModalDeleteView

from .forms import CategoryForm
from .models import  Category


categories_home = lambda request: render(request, 'categories/index.html')

category = lambda request, pk: render(request, 'categories/index.html#category', {'category': Category.objects.get(id=pk)})

category_list = lambda request: render(request, 'categories/index.html#category-list', {'categories': Category.objects.order_by('name')})


class CategoryCreateView(HTMXModalCreateView):
    model = Category
    template_name = 'categories/index.html#category-form'
    form_class = CategoryForm
    url_name = 'categories:create'


class CategoryUpdateView(HTMXModalUpdateView):
    model = Category
    template_name = 'categories/index.html#category-form'
    form_class = CategoryForm
    url_name = 'categories:update'


class CategoryDeleteView(HTMXModalDeleteView):
    model = Category
    template_name = 'categories/index.html#category-form'
    url_name = 'categories:delete'
