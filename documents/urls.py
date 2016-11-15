from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)$', views.DocumentDetailView.as_view(), name='document_detail'),
]
