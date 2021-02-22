from django.urls import path,include
from api import views
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("customerApi", views.customerApi)
router.register("orderApi", views.ordersApi)


urlpatterns = [
    path('',include(router.urls)),
    path('auth/', include('rest_framework_social_oauth2.urls')),
    path('sms',views.sendSms),
    path('api-auth/', include('rest_framework.urls')),
]
