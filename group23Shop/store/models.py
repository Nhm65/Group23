from django.db import models

class Orders(models.Model):
    id=models.AutoField
    customer_id=models.CharField(max_length=255)
    order_date=models.DateTimeField
    total_amount=models.CharField(max_length=255)

class Order_Details(models.Model):
    id=models.AutoField
    order_id=models.CharField(max_length=255)
    product_id=models.CharField(max_length=255)
    quantity=models.CharField(max_length=255)
    price=models.CharField(max_length=255)
# Create your models here.
