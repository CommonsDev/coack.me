from django.conf.urls import patterns, include, url

from .views import ProfileDetailView

urlpatterns = patterns('',
    url(r'(?P<username>(?!signout|signup|signin)[\.\w-]+)/$',
        ProfileDetailView.as_view(),
        name='profile-detail'),
)
