from rest_framework import routers

from .views import *


router = routers.DefaultRouter()

router.register('check_bullying', CheckBullyingViewSet, basename='check_bullying')
