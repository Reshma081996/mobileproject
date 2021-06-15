from django.db import models


# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=120)
    price = models.FloatField()
    specs = models.CharField(max_length=120)
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.product_name

# makemigrtaions will create a migrateionfile that contain convrted equvalent queries acc to database connected
# migrate -execute Quries( to create the table here)

class Orders(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    user = models.CharField(max_length=120)
    choices = (
        ("Ordered","Ordered"),
        ("Cancelled","Cancelled"),
        ("Delivered","Delivered")
)
    status = models.CharField(max_length=12,choices=choices,default="ordered")

class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    user = models.CharField(max_length=120)
    price_total = models.IntegerField(editable=False,blank=True,null=True)