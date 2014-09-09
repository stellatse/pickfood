import datetime
from django.db import models
from django.utils import timezone
# Define table models.


class User(models.Model):
    uid = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    verified = models.BooleanField(default=False)
    start_time = models.DateTimeField(auto_now_add=True)
    verified_time = models.DateTimeField(auto_now=True)
    system = models.BooleanField(default=False)  # if user is a system admin
    role = models.IntegerField(default=0)  # user role, 0: normal, 1: advantage
    pay_account = models.CharField(max_length=20)


class ShopList(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=20)
    add_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Shop(models.Model):
    shop_list = models.ForeignKey(ShopList)
    name = models.CharField(max_length=20)
    add_time = models.DateTimeField(auto_now_add=True)
    last_time = models.DateTimeField(auto_now=True)
    picked_times = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def was_picked_recently(self):
        return self.last_time >= timezone.now() - datetime.timedelta(days=3)





