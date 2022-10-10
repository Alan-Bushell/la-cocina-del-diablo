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


class Event(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, null=True)
    date = models.DateField(blank=False)
    time = models.TimeField(blank=False)
    tickets_available = models.IntegerField()
    featured_image = CloudinaryField('image', default='placeholder')
    description = models.TextField()
    excerpt = models.TextField(blank=True)
    event_added = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="events")
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-event_added']

    def __str__(self):
        return self.title


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
