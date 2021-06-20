from django.db import models

# Create your models here.


class Product(models.Model):

    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcatagory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default="")
    desc = models.CharField(max_length=50)
    pub_date = models.DateField(default="")
    image = models.ImageField(upload_to='images', default="")

    def __str__(self):
        return self.product_name


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.IntegerField()
    query = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Order(models.Model):
    order_id= models.AutoField(primary_key=True) 
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state= models.CharField(max_length=50)
    pincode= models.CharField(max_length=50)
    phone = models.IntegerField()

    def __str__(self):
        return self.name, self.order_id 