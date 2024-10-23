from django.urls import path
from .views import save_scene

urlpatterns = [
    path('api/save_scene/', save_scene, name='save_scene'),
]
