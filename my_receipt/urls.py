from django.urls import path, include
from . views import *
# from rest_framework_nested import routers 

# router = routers.DefaultRouter()
# router.register('receipt', PaymentReceiptViewSet, basename='receipt_gateway')

urlpatterns= [
    # path('', include(router.urls)),
    path('receipt/', PaymentReceiptViewSet.as_view())
]