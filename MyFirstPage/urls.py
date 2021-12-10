from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from firstsite.sitemaps import StaticViewSitemap
from Blog.sitemaps import BlogSitemap

sitemaps = {
    'static': StaticViewSitemap,
    'Blog':BlogSitemap
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('firstsite.urls')),
    path('',include('Blog.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', include('robots.urls')),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)