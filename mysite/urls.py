"""mysite URL Configuration

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
from django.conf.urls import url
from . import view
from . import testdb
from . import search
from . import search2
# from django.contrib import admin
#
# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
# ]
urlpatterns = [
    url(r'^hello/$', view.hello),
    url(r'^insertdb/$', testdb.insertdb),
    url(r'^getdb/$', testdb.getdb),
    url(r'^updatedb/$', testdb.updatedb),
    url(r'^deletedb/$', testdb.deletedb),
    url(r'^search/$', search.search),
    url(r'^search_form/$', search.search_form),
    url(r'^search_post/$', search2.search_post),
]

