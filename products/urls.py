from django.urls import path
<<<<<<< HEAD

from .views import ProductDetailView

urlpatterns = [
    path('/productdetail', ProductDetailView.as_view())
]
=======
from .views      import ProductListView

urlpatterns = [
    path('/productlist', ProductListView.as_view()),
]
>>>>>>> main
