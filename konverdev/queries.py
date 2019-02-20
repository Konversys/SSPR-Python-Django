from django.db import connection

from .models import *

def GetWagons():
    return Wagon.objects.raw("SELECT * from wagon")

def ClearWagon(wagon):
    with connection.cursor() as c:
        c.execute("delete from stock where wagon = %s" % wagon)

def ChangeCountProductToWagon(wagon, product, count):
    with connection.cursor() as c:
        c.execute("UPDATE stock SET selled = selled + %s where wagon = %s and product = %s" % (count, wagon, product))
                     
def UpdateStock(wagon, product, count):
    with connection.cursor() as c:
        c.execute("INSERT INTO stock(wagon, product, count, selled) VALUES(%s, %s, %s, 0) ON DUPLICATE KEY UPDATE count = count + %s" % (wagon, product, count, count))

def GetWagon(wagon):
    return StockView.objects.raw("SELECT stock.wagon as wagon, stock.product as product, product.title as title, product.price as price, stock.count as count, stock.selled as selled, stock.selled * product.price as total from stock, product where stock.product = product.id and stock.wagon = %s" % wagon)

def GetProducts():
    return ProductView.objects.raw("select product.id, product.title, tag.title as tag, product.price, product.unit, product.img_path from product, tag where product.tag = tag.id")

def InsertProduct(title, tag, img_path, price, unit):
    with connection.cursor() as c:
        c.execute("INSERT INTO product (title, price, tag, img_path, unit) VALUES(\"%s\", %s, %s, \"%s\", \"%s\")" % (title, price, tag, img_path, unit))

def UpdateProduct(id, title, tag, img_path, price, unit):
    with connection.cursor() as c:
        c.execute("UPDATE product SET title = \"%s\", tag = %s, img_path = \"%s\", price = %s, unit = \"%s\" where id = %s" % (title, tag, img_path, price, unit, id))

def GetProduct(id):
    return Product.objects.raw("select * from product where id = %s" % id);

def GetTags():
    return Tag.objects.raw("select * from tag")

def DeleteProduct(id):
    with connection.cursor() as c:
        c.execute("delete from product where id = %s" % id)