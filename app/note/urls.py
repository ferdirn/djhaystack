from django.conf.urls import patterns, url

from app.note import views

urlpatterns = patterns('',
    # /note
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
)