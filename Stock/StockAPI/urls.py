from django.conf.urls import patterns, include, url
#from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from StockAPI import views

urlpatterns = patterns('',
url(r'^item/$', views.ItemList.as_view()),
url(r'^item/(?P<pk>\d+)/$', views.ItemDetail.as_view()),
url(r'^transaction/$', views.TransactionList.as_view()),
url(r'^transaction/(?P<pk>\d+)/$', views.TransactionDetail.as_view()),
)
urlpatterns = format_suffix_patterns(urlpatterns)