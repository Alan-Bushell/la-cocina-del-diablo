from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# Create your models here.

STATUS = ((0, "Not Live"), (1, "Live"))


class Menu(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True)
    image = CloudinaryField('image', default='placeholder')
    description = models.TextField()
    set_menu = models.BooleanField()
    if set_menu:
        price = models.IntegerField()
    status = models.IntegerField(choices=STATUS, default=0)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.name


class Starter(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    price = models.IntegerField()


class MainDish(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    price = models.IntegerField()


class Dessert(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    price = models.IntegerField()
