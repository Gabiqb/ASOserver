from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('aso/', include('aso.urls')),
    path('', include('aso.urls')),
    path('admin/', admin.site.urls),
]