from django.urls import path

from .views import checkout


urlpatterns = [
    # path('checkout/', CartListView.as_view, name='checkout'),
    path('checkout/', checkout, name='checkout'),
]
