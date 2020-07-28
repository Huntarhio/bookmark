from django.conf.urls import include, url
from . import views

app_name = "images"

urlpatterns = [
    url(r'^create/$', views.image_create_formview, name="image_create"),
    url(r'^detail/(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.image_detail, name='image_detail'),
]