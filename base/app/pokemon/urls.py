# django imports
from django.urls import path
from django.urls import include
# DRF imports
from rest_framework.routers import DefaultRouter
# view imports
from pokemon import views


router = DefaultRouter()
router.register(r'pokemon', views.PokemonViewSet)


app_name = 'pokemon'

urlpatterns = [
    path('', include(router.urls))
]
