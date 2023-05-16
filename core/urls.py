from django.urls import path, include
# from django.urls.conf import include
from . views import *
from rest_framework_nested import routers 

router = routers.DefaultRouter()
router.register('page', SignUpPage, basename='register')

urlpatterns= [
    path('', include(router.urls)),
    path('login/', LoginPage.as_view())
]