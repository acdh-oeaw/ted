from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers

from vocabs import api_views

router = routers.DefaultRouter()
router.register(r'skoslabels', api_views.SkosLabelViewSet)
router.register(r'skosnamespaces', api_views.SkosNamespaceViewSet)
router.register(r'skosconceptschemes', api_views.SkosConceptSchemeViewSet)
router.register(r'skosconcepts', api_views.SkosConceptViewSet)


urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
    url(r'^', include('webpage.urls', namespace='webpage')),
    url(r'^vocabs/', include('vocabs.urls', namespace='vocabs')),
    url(r'^datamodel/', include('django_spaghetti.urls', namespace='datamodel')),
    url(r'documents/', include('documents.urls', namespace='documents')),
    url(r'browsing/', include('browsing.urls', namespace='browsing')),
    url(r'charts/', include('charts.urls', namespace='charts')),
]
