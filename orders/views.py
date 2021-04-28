import json

from django.http      import JsonResponse
from django.views     import View

from user.models    import User
from user.utils     import login_decorator
from product.models import (
    OrderItem,
)
from order.models   import OrderProduct, Order, OrderStatus
# from user.utils     import login_decorator

class CartView(View):
    # @login_decorator
    def post(self, request, *args, **kwargs):
        try:
            data         = json.loads(request.body)
            user         = request.user
            product_id   = data['productId']
            total_price  = data['totalPrice']
            quantity     = data['quantity']
            order_status = OrderStatus.objects.get(name=SHOPPING_BASKET)