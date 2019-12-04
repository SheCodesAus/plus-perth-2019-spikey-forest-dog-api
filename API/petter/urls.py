from django.urls import path, include
from . import views
from django.conf.urls import url
from rest_framework import routers

router = routers.DefaultRouter()
# Returns individual user profiles
router.register(r'profiles', views.ProfileViewSet)
# Returns a list of all users, GET requests
router.register(r'users', views.UserViewSet)
#  Use for POST requests to register a new user
# router.register(r'register', views.RegisterViewSet)
# router.register(r'pets', views.PetViewSet)

urlpatterns = [
    path('', include(router.urls)),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
]