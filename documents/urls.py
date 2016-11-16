from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        r'^document/(?P<pk>[0-9]+)$', views.DocumentDetailView.as_view(),
        name='document_detail'),
    url(
        r'^archobject/(?P<pk>[0-9]+)$', views.ArchObjectDetailView.as_view(),
        name='archobject_detail'),
    url(
        r'^digobject/(?P<pk>[0-9]+)$', views.DigObjectDetailView.as_view(),
        name='digobject_detail'),
]
