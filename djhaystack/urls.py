from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import RedirectView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djhaystack.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', RedirectView.as_view(url='note/', permanent=False), name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^note/', include('app.note.urls', namespace='note')),
    url(r'^search/', include('haystack.urls')),
)
