from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('pessoas.urls')),
    path('pessoas/', include('pessoas.urls')),
    path('admin/', admin.site.urls),
]
