from django.conf.urls import url
from . import api


urlpatterns = [
    url(r'^visitor/$', api.VisitorList.as_view()),
    url(r'^visitor/(?P<pk>[0-9]+)/$', api.VisitorDetail.as_view())
]
