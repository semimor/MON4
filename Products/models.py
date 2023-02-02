from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    image = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    rate = models.FloatField()
    create_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)
    commentable = models.BooleanField(default=True)


class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    text = models.CharField(max_length=255)
    created_date = models.DateField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)