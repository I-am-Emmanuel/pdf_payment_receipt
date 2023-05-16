from rest_framework import serializers

from . models import *
# from . goods import *


from core.models import UserModel

class SimpleCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['id', 'first_name', 'last_name']


class PaymentReceiptSerializer(serializers.ModelSerializer):
    customer = SimpleCustomerSerializer()
    class Meta:
        model = PaymentReceipt
        fields = ['customer', 'amount', 'items_purchased', 'date']

        read_only_fields = ['customer']






















    # def create(self, validated_data):
    #     instance = self.Meta.model(**validated_data)
    #     instance.items_purchased = product()
    #     instance.amount = payment()
    #     instance.save()
    #     return instance