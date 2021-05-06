import json

from django.http      import JsonResponse
from django.views     import View

from json             import JSONDecodeError

from user.models    import User
from user.utils     import login_decorator
from product.models import (
    OrderItem,
)
from order.models   import OrderProduct, Order, OrderStatus
# from user.utils     import login_decorator

SHOPPING_BASKET = "장바구니"

class CartView(View):
    # @login_decorator
    def post(self, request, *args, **kwargs):
        try:
            data         = json.loads(request.body)
            user         = request.user
            product_id   = data['productId']
            price        = data['price']
            quantity     = data['quantity']
            order_status = OrderStatus.objects.get(name=SHOPPING_BASKET)

            if not Order.objects.filter(user=user, status=order_status_code).exists():
                order = Order.objects.create(
                    user   = user,
                    status = order_status_code
                )
                OrderItem.objcects.create(
                order                  = order,
                product_id             = product_id,
                order_item_status_code = order_item_status_code,
                quantitiy              = quantity,
                price                  = price
                )
                return JsonResponse({'message' : 'SUCCESS'}, status=200)

            order = Order.objects.get(user=user, status=order_status_code)
            if not OrderItem.objects.filter(order=order, product_id=product_id).exists():
                OrderItem.objects.create(
                    order                  = order,
                    product_id             = product_id,
                    quantity               = quantity,
                    price                  = price,
                    order_item_status_code = order_item_status_code
                )
                return JsonResponse({'message', 'SUCCESS'}, status=200)
            
            order_item            = OrderItem.objects.get(order=order, product_id=product_id)
            order_item.quantitiy += int(quantity)
            order_item.price     += int(price)
            order_item.save()

            return JsonResponse({'message': 'SUCCESS'}, status=200)

        except JSONDecodeError:
            return JsonResponse({'message': 'BAD_REQUEST'}, status=400)

        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)

        except Product.DoesNotExist:
            return JsonResponse({'message': 'DOES_NOT_EXIST'}, status=400)

        except Order.DoesNotExist:
            return JsonResponse({'message': 'DOES_NOT_EXIST'}, status=400)

        except Order.MultipleObjectsReturned:
            return JsonResponse({'message': 'MULTIPLE_OBJECTS_RETURNED'}, status=400)
        
    #@login_decorator
    def get(self, request, *args, **kwargs):
        try:
            user         = request.user
            order        = Order.objects.get(user=user, status__name=SHOPPING_BASKET)
            cart_lists   = order.order_item_set.all()
            result = [
                {
                    'cartId'    : cart_list.id,
                    'productId' : cart_list.product_id,
                    'product'   : cart_list.product.name,
                    'option'    : cart_list.option,
                    'quantity'  : cart_list.quantity,
                    'totalPrice': int(cart_list.total_price),
                    'eachPrice' : cart_list.product.price,
                    'urlImage'  : cart_list.product.image_url,
                } for cart_list in cart_lists
            ]
            return JsonResponse({'message': 'SUCCESS', 'result': result}, status=200)

        except Order.DoesNotExist:
            return JsonResponse({'message': 'DOES_NOT_EXIST'}, status=400)

    #@login_decorator
    def delete(self, request, *args, **kwargs):
        try:
            cart_id_list = request.GET.getlist('cartId', None)
            int_cart_id  = [int(cart_id) for cart_id in cart_id_list]
            cart         = Cart.objects.filter(id__in=int_cart_id)
            if not cart.exists():
                return JsonResponse({'message': 'DOES_NOT_EXIST'}, status=400)

            cart.delete()
            return JsonResponse({'message': 'SUCCESS'}, status=200)

        except JSONDecodeError:
            return JsonResponse({'message': 'BAD_REQUEST'}, status=400)

        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)

        except Order.DoesNotExist:
            return JsonResponse({'message': 'DOES_NOT_EXIST'}, status=400)

        except OrderStatus.DoesNotExist:
            return JsonResponse({'message': 'DOES_NOT_EXIST'}, status=400)