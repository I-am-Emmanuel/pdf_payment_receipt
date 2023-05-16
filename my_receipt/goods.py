import random
from decimal import Decimal as dec

def product():
    item = random.choices(['Television', 'Laptop', 'Air-Conditioner', 'Refrigerator'])
    return item[0]


def payment():
    goods_paid = random.randint(100, 999999)
    return goods_paid
