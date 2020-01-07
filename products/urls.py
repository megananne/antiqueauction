"""antqiue_auction URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from .views import *


urlpatterns = [
    url(r'^$', index, name='products'),
    url(r'^$', index, name='index'),
    url(r'^products$', products, name='products'),
    url(r'^all_antiques$', products, name='products'),
    url(r'^art$', products, name='art'),
    url(r'^classic_cars$', products, name='classic cars'),
    url(r'^clocks$', products, name='clocks'),
    url(r'^furniture$', products, name='furniture'),
    url(r'^jewellery$', products, name='jewellery'),
    url(r'^toys$', products, name='toys'),
]
