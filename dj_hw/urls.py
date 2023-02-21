from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),
    path('', include('user.urls')),
    path('', include('cart.urls')),
    path('', include('product.urls')),
    path('', include('admin_view.urls')),
]
