from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'documents/$', views.DocumentListView.as_view(), name='browse_documents'),
    url(r'archobjects/$', views.ArchObjectListView.as_view(), name='browse_archobjects'),
    url(r'digobjects/$', views.DigObjectListView.as_view(), name='browse_digobjects'),
]
