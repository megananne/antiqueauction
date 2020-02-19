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
from django.conf.urls import url
from django.contrib import admin
from home.views import index
from accounts import urls as urls_accounts
from products import urls as urls_products
from checkout import urls as urls_checkout
from cart import urls as urls_cart
from home import urls as urls_home
from home.views import terms
from home.views import support
from home.views import reviews
from home.views import about
from accounts.views import login
from accounts.views import profile
from accounts.views import register
from django.views.static import serve
from .settings import MEDIA_ROOT



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^$', index, name='index'),
    url(r'^terms/$', terms),
    url(r'^support/$', support),
    url(r'^reviews/$', reviews),
    url(r'^login/$', login),
    url(r'^profile/$', profile),
    url(r'^register/$', register),
    url(r'^accounts/', include(urls_accounts)),
    url(r'^products/', include(urls_products)),
    url(r'^home/', include(urls_home)),
    url(r'^about/', about),
    url(r'^$', include(urls_home)),
    url(r'^checkout/', include(urls_checkout)),
    url(r'^cart/', include(urls_cart)),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT }),


]
