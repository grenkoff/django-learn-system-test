from django.contrib.auth.models import User
from django.db import models

class Product(models.Model):  # поле id  наследуется от Model
    title = models.CharField(max_length=32)
    user = models.ForeignKey(User, models.PROTECT) # создаем связь с юзером через ForeignKey # продукт не удалится из-за удаления юзера


class ProductAccess(models.Model):
    user = models.ForeignKey(User, models.PROTECT)
    product = models.ForeignKey(Product, models.PROTECT, 'accesses')
    is_valid = models.BooleanField(default=True)