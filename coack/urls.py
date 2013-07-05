from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.views.generic import TemplateView

from .views import RootRouter

urlpatterns = patterns('',
    url(r'^$', RootRouter.as_view(), name='root'),
    url(r'^home$', TemplateView.as_view(template_name='index.html'), name='home'),
                       
    url(r'^', include('social_auth.urls')),                       
    url(r'^', include('accounts.urls')),

    url(r'^s/', include('services.urls')),
    url(r'^feedback/', include('backcap.urls')),
)

urlpatterns += i18n_patterns('',
    url(r'^admin/', include(admin.site.urls)),                                                          
    url(r'^', include('cms.urls'))
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

