from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.i18n import url, i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin

from isodur_app import views

urlpatterns = [
    url(r'^i18n', include('django.conf.urls.i18n'))
]

urlpatterns += i18n_patterns(
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^company/$', views.CompanyView.as_view(), name='company'),
    url(r'^product-1/$', views.ProductListView.as_view(), name='product1'),
    url(r'^product-2/$', views.Product2.as_view(), name='product2'),
    url(r'^product-3/$', views.Product3.as_view(), name='product3'),
    url(r'^projects/$', views.ProjectListView.as_view(), name='project_list'),
    url(r'^contacts/$', views.contacts, name='contacts'),
    url(r'^admin/',  include(admin.site.urls)),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^rosetta/', include('rosetta.urls')),
    url(r'^video/$', views.ProjectVideoView.as_view(), name='project_video'),
    prefix_default_language=False
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
