from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    (r'^index/', TemplateView.as_view(template_name="index.html")),
    (r'^$', TemplateView.as_view(template_name="index.html")),
    (r'^recipes/southern_fried_chicken', TemplateView.as_view(template_name="recipes/southern_fried_chicken.html")),
    (r'^chefs/gordon_ramsay', TemplateView.as_view(template_name="chefs/gordon_ramsay.html")),
    (r'^chefs/', TemplateView.as_view(template_name="chefs.html")),
)
