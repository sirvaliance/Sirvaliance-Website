from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'home.views.index', name='home'),
    url(r'^mozilla/$', 'home.views.mozilla', name='home'),
	url(r'^sir-valiance-start', 'home.views.ob_start'),
	url(r'^mobius', 'home.views.ob_mobius'),
	url(r'^sir-valiance-quantico', 'home.views.ob_quantico'),
	url(r'^a-fresh-start', 'home.views.ob_fresh'),
	url(r'^robots.txt', 'home.views.robots'),
	url(r'^four/', 'home.views.four'),

    # url(r'^sirvaliance/', include('sirvaliance.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
