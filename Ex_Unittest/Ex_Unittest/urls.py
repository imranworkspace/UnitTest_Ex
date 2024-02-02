from django.contrib import admin
from django.urls import path
from products import views as v
urlpatterns = [
    path('admin/', admin.site.urls),
    path('prod/',v.all_products),
]