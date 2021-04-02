from django.db import models

class User(models.Model):
    email       = models.CharField(max_length=45, unique=True)
    password    = models.CharField(max_length=300)
    name        = models.CharField(max_length=45)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'users'