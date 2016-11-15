from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'documents/$', views.DocumentListView.as_view(), name='browse_documents'),
]
