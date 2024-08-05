from django.urls import path
from . import views

app_name = "products"

urlpatterns = ()

urlpatterns += (
    path('product/api/create/', views.ProductCreateAPIView.as_view(), name='product_create_api'),
    path('product/api/<int:pk>/update/', views.ProductUpdateAPIView.as_view(), name='product_update_api'),
    path('product/api/<int:pk>/', views.ProductDetailAPIView.as_view(), name='product_detail_api'),
    path('product/api/<int:pk>/delete/', views.ProductDeleteAPIView.as_view(), name='product_delete_api'),
)

