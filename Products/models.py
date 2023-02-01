from django.db import models

# Create your models here.
class Product(models.Model):
    image = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    rate = models.FloatField()
    create_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)
    

class Review(models.Model):
    text = models.CharField(max_length=255)
    created_date = models.DateField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)