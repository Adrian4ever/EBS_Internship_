from django.urls import path

from store.views import ProductsItemView, ProductsListView, ImageViewSet

urlpatterns = [
    path('products/', ProductsListView.as_view(), name='Products_list'),
    path('product/<int:pk>/', ProductsItemView.as_view(), name='Product_item'),
    path('upload/', ImageViewSet.as_view(), name='upload'),
]
