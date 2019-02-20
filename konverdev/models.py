from django.db import models


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64)
    price = models.FloatField()
    tag = models.IntegerField()
    unit = models.CharField(max_length=64)
    img_path = models.CharField(max_length=1024)


class ProductView(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64)
    tag = models.CharField(max_length=64)
    price = models.FloatField()
    unit = models.CharField(max_length=64)
    img_path = models.CharField(max_length=1024)


class Stock(models.Model):
    class Meta:
        unique_together = (('wagon', 'product'),)
    wagon = models.IntegerField(primary_key=True)
    product = models.IntegerField()
    count = models.IntegerField()
    selled = models.IntegerField()


class StockView(models.Model):
    class Meta:
        unique_together = (('wagon', 'product'),)
    wagon = models.IntegerField(primary_key=True)
    product = models.IntegerField()
    title = models.CharField(max_length=64)
    count = models.IntegerField()
    selled = models.IntegerField()
    total = models.FloatField()

class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64)


class Wagon(models.Model):
    id = models.AutoField(primary_key=True)
    number = models.IntegerField()
