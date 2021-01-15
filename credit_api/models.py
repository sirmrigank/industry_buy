from django.db import models


# Create your models here.


class Bank_details(models.Model):
    name = models.CharField(max_length=100)
    walletid = models.IntegerField(max_length=100, unique=True)
    amount = models.IntegerField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Transaction_detail(models.Model):
    name_from = models.CharField(max_length=100, default='self')
    name_to = models.CharField(max_length=100, default='self')
    walletid_from = models.IntegerField(max_length=100, default=0)
    walletid_to = models.IntegerField(max_length=100, default=0)
    amount_credit = models.IntegerField(max_length=100, default=0)
    amount_debit = models.IntegerField(max_length=100, default=0)
    updated_balance = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)


class user_monthly_details(models.Model):
    name = models.CharField(max_length=100)
    walletid = models.IntegerField(max_length=100)
    amount_add = models.IntegerField(max_length=100, default=0)
    amount_debit = models.IntegerField(max_length=100, default=0)
