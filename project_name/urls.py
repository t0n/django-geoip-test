from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'project_name.app_name.views.home', name='home'),
)
