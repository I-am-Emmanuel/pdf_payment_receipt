from django.contrib import admin
from . models import *

# Register your models here.
@admin.register(PaymentReceipt)
class ReceiptModel(admin.ModelAdmin):
    list_display = ['first_name', 'amount', 'items_purchased', 'date']
