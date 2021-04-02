from django.db import models

from users.models       import User
from products.models    import Product

class Order(models.Model):
    user              = models.ForeignKey('users.User', on_delete=models.CASCADE)
    created_at        = models.DateTimeField(auto_now_add=True)
    order_status_code = models.ForeignKey('OrderStatusCode', on_delete=models.CASCADE)

    class Meta:
        db_table = 'orders'

class OrderStatusCode(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'order_status_codes'

class OrderItem(models.Model):
    order                  = models.ForeignKey('Order', on_delete=models.CASCADE)
    product                = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    order_item_status_code = models.ForeignKey('OrderItemStatusCode', on_delete=models.CASCADE)
    quantity               = models.IntegerField()
    price                  = models.DecimalField(decimal_places=2, max_digits=10)
    
    class Meta:
        db_table = 'order_items'

class OrderItemStatusCode(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'order_item_status_codes'

class Shipment(models.Model):
    order           = models.ForeignKey('Order', on_delete=models.CASCADE)
    tracking_number = models.IntegerField()
    date            = models.DateTimeField(auto_now_add=True)
    other_detail    = models.TextField()

    class Meta:
        db_table = 'shipments'




