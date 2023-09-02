from django.urls import path
from . import views


app_name = 'categories'

urlpatterns = [
    path('', views.categories_home, name='home'),
    path('new', views.CategoryCreateView.as_view(), name='create'),
    path('category-list', views.category_list, name='category-list'),
    path('<int:pk>', views.category, name='category'),
    path('<int:pk>/update', views.CategoryUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', views.CategoryDeleteView.as_view(), name='delete'),
]