from django.urls import path
from .views import ndvi_view

urlpatterns = [
    path('', ndvi_view, name='ndvi_view')
]
