from django.conf.urls import include, url
from . import views
from django.conf import settings

urlpatterns = [
    url(r'^$', views.compra),
    url(r'^media/(?P<path>.*)$','django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

]
