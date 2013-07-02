from django.conf.urls import patterns, include, url

from .views import ServiceAddView, ServiceDeleteView

urlpatterns = patterns('',
    # Examples:
    url(r'^add$', ServiceAddView.as_view(), name='service-add'),
    url(r'^(?P<pk>\d+)/del/$', ServiceDeleteView.as_view(), name='service-del')
)
