import json

from django.http  import JsonResponse
from django.views import View

from users.models      import User
# from users.utils     import login_decorator
from products.models   import Product

class ProductListView(View):
    # @login_decorator
    def get(self, request):
        products = Product.objects.all()
        
        product_list = []
        for product in products:
            dict = {
                'id': product.id,
                'name': product.name,
                'sub_name': product.sub_name,
            }
            product_list.append(dict)
        return JsonResponse({"product": product_list}, status=200)