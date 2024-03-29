from django.db import models
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
# Create your models here.

STATUS = ((0, "Not Live"), (1, "Live"))
BOOKING_STATUS = ((0, "Awaiting Confirmation"), (1, "Confirm Booking"),
                  (2, "Booking Declined"))


# Customer model extending base user model
class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=40, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    contact_phone = models.CharField(max_length=15, null=True, blank=True)
    profile_image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        if self.user:
            return f"{self.first_name + ' ' + self.last_name}"
        else:
            return f"New Customer / Not Provided"


# Booking model for when making a reservation
class Booking(models.Model):
    email = models.EmailField()
    contact_phone = models.CharField(max_length=15, null=False, blank=False)
    booking_date = models.DateField(null=False, blank=False)
    booking_time = models.CharField(null=False, blank=False, max_length=5)
    number_of_attendees = models.IntegerField(default=2, blank=False)
    booking_status = models.IntegerField(choices=BOOKING_STATUS, default=0)
    customer = models.ForeignKey('Customer', null=True, on_delete=models.CASCADE)

    def __str__(self):
        if self.customer:
            return f"Booking for {self.customer}"
        else:
            return f"Booking (Customer or User not specified)"


# Event model
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


# Menu model to house each menu
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


# Starter model
class Starter(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    price = models.IntegerField()
    menu = models.ForeignKey(Menu, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


# Main dish model
class MainDish(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    price = models.IntegerField()
    menu = models.ForeignKey(Menu, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


# Desserts model
class Dessert(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    price = models.IntegerField()
    menu = models.ForeignKey(Menu, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


# Signal used to create customer once user created
@receiver(post_save, sender=User)
def create_user_customer(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(user=instance)


# Signal used to save the customer if user is saved
@receiver(post_save, sender=User)
def save_user_customer(sender, instance, created, **kwargs):
    instance.customer.save()
