from django.urls import include, path
from django.conf.urls import include, url
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
#router.register(r'heroes', views.HeroViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'.*', views.gateway.as_view())
]