from django.urls import path

from .views import visitorform,base1

urlpatterns = [
    path('form/', visitorform),
    path('', base1)
    # ... more URL patterns here
]