from django.db import models

from users.models import User

class Category(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'categories'

class SubCategory(models.Model):
    name     = models.CharField(max_length=45)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    class Meta:
        db_table = 'sub_categories'

class Product(models.Model):
    sub_category = models.ForeignKey('SubCategory', on_delete=models.CASCADE)
    name            = models.CharField(max_length=45, unique=True)
    sub_name        = models.CharField(max_length=200, unique=True)
    price           = models.DecimalField(decimal_places=2, max_digits=10)
    created_at      = models.DateTimeField(auto_now_add=True)
    unit_of_sale    = models.CharField(max_length=45)
    volume          = models.CharField(max_length=45)
    delivery_type   = models.CharField(max_length=45)
    packing_type    = models.CharField(max_length=45)
    content         = models.TextField()

    class Meta:
        db_table = 'products'

class ProductExtraInfomation(models.Model):
    field   = models.CharField(max_length=100)
    value   = models.CharField(max_length=800)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'product_extra_informations'

class ProductImage(models.Model):
    image_url = models.CharField(max_length=255)
    product   = models.ForeignKey('Product', on_delete=models.CASCADE)

    class Meta:
        db_table = 'product_images'

class ProductReview(models.Model):
    user       = models.ForeignKey('users.User', on_delete=models.CASCADE)
    product    = models.ForeignKey('Product', on_delete=models.CASCADE)
    content    = models.CharField(max_length=100)
    image_url  = models.CharField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'product_reviews'
