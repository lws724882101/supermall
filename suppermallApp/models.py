from django.db import models
import os
# Create your models here.

class HomeGoods(models.Model):
    GoodsName = models.CharField(max_length=100,null=True)
    GoodsPhoto = models.CharField(max_length=50,null = True)
    GoodsPrice = models.FloatField(max_length=50,null=False)
    Page = models.SmallIntegerField(null=False)
    CollectionCount = models.IntegerField(null=True,default=0)


class Banner(models.Model):
    width = models.SmallIntegerField(null=True,default=750)
    height = models.SmallIntegerField(null=True,default=390)
    title = models.CharField(max_length=150)
    imageUrl = models.CharField(max_length=100)

class Recommend(models.Model):
    title = models.CharField(max_length=150)
    imageUrl = models.CharField(max_length=100)

