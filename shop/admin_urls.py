"""MyDigShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path
from shop.admin_views import goods_mass_load, goods_textform, goods_fileform


urlpatterns = [
    re_path('admin/shop/goods_mass_load/$', goods_mass_load),
    re_path('admin/shop/goods_mass_load/add_text/$', goods_textform),
    re_path('admin/shop/goods_mass_load/add_file/$', goods_fileform),
]