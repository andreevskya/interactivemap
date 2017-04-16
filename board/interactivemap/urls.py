from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^floor/(?P<number>[0-9]?)$', views.floor, name='floor'),
    url(r'^search', views.search, name='search'),
    url(r'^rest', include('interactivemap.rest_urls')),
    url(r'^pages/', include('django.contrib.flatpages.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
