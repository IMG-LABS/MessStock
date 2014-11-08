from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Stock.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^StockAPI/', include('StockAPI.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
