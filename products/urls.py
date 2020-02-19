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
    url(r'^$', products, name='products'),
    url(r'^art/$', get_art, name='art'),
    url(r'^classiccars/$', get_classiccars, name='classiccars'),
    url(r'^clocks/$', get_clocks, name='clocks'),
    url(r'^furniture/$', get_furniture, name='furniture'),
    url(r'^jewellery/$', get_jewellery, name='jewellery'),
    url(r'^toys/$', get_toys, name='toys'),

]