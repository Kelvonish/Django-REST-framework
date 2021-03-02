from django.urls import path,include
from api import views
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("customerApi", views.customerApi)
router.register("orderApi", views.ordersApi)


urlpatterns = [
    path('browsableApi/',include(router.urls),name="browsableApi"),
    path('auth/', include('rest_framework_social_oauth2.urls')),
    path('',views.Login,name="login"),
    path('logout',views.logout_view,name="logout"),
    path('createCustomer',views.createUser,name="createCustomer"),
    path('api-auth/', include('rest_framework.urls')),
]
