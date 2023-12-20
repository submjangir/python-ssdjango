from django.db import models

# Create your models here.

class Registration(models.Model):
    first_name = models .CharField(max_length=100,default="",null=True)
    last_name = models .CharField(max_length=100,default="",null=True)
    email = models .CharField(max_length=100,default="",null=True)
    password = models .CharField(max_length=255,default="",null=True)
    mobile = models .BigIntegerField(default=1)
    gender = models .CharField(max_length=100,default="",null=True)

    def __str__(self):
       return self.first_name
    


class Category(models.Model):
    category_image = models.ImageField(upload_to="upload/category/")
    category_name = models.CharField(max_length=100,default="", null=True)

    def __str__(self):
        return self.category_name
    

class Product(models.Model):
    product_image = models.ImageField(upload_to="upload/product/")
    product_name = models.CharField(max_length=100, default="", null=True)
    product_price = models.IntegerField(default=1)
    product_description = models.TextField(blank=True, max_length=200, null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name
    


class Order(models.Model):
    address = models.CharField(max_length=200,default="", null=True)
    mobile = models.BigIntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Registration, on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField()
    status = models.BooleanField()

    def __str__(self):
       return self.product.product_name