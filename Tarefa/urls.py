from django.contrib import admin
from django.urls import path
from base.views import inicio, tabela

urlpatterns = [
    path('', inicio),
    path('tabela/', tabela),
    path('admin/', admin.site.urls),
]
