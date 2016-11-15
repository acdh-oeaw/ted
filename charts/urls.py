from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^barcharts/$', views.barcharts_view, name='bar_charts'),
    url(r'^piecharts/$', views.piecharts_view, name='pie_charts'),
    url(r'^documenttypes/$', views.documenttype_json, name='documenttype_json'),
]
