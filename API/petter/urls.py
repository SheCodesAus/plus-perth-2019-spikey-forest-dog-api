from django.urls import path, include
from . import views
from django.conf.urls import url
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'profiles', views.ProfileViewSet)
router.register(r'users', views.UserViewSet)
# router.register(r'pets', views.PetViewSet)

urlpatterns = [
    path('', include(router.urls)),
]