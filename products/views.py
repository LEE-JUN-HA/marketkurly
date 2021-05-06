import json

from django.http  import JsonResponse
from django.views import View

from users.models      import User
# from users.utils     import login_decorator
from products.models   import Product

class ProductDetailView(View):
    # @login_decorator
    def get(self, request):
        products = Product.objects.all()

        product_list = []
        for product in products:
            dict = {
                'id'            : product.id,
                'name'          : product.name,
                'sub_name'      : product.sub_name,
                'price'         : product.price,
                'cotent'        : product.content,
                'unit_of_sale'  : product.unit_of_sale,
                'volume'        : product.volume,
                'delivery_type' : product.delivery_type,
                'packing_type'  : product.packing_type,
                'image_url'     : [productimage.image_url for productimage in product.productimage_set.all()],
            }
            product_list.append(dict)
        return JsonResponse({"products": product_detail}, status=200) 
