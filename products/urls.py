from django.urls import path

from .views import ProductDetailView
from .views import ProductListView

urlpatterns = [
    path('/productdetail', ProductDetailView.as_view()),
    path('/productlist', ProductListView.as_view()),
]
