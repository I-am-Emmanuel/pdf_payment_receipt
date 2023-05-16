from django.db import models
from django.contrib import admin
from django.conf import settings

# Create your models here.

class PaymentReceipt(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    items_purchased = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self)-> str:
        return self.customer.first_name

    def __str__(self)-> str:
        return self.date

    @admin.display(ordering='customer__first_name')
    def first_name(self)-> str:
        return f'{self.customer.first_name}'

    class Meta:
        ordering = ['customer__first_name']