from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from firstsite.sitemaps import StaticViewSitemap
from Blog.sitemaps import BlogSitemap
import debug_toolbar
from django.contrib.auth import views as auth_views


sitemaps = {
    'static': StaticViewSitemap,
    'Blog': BlogSitemap
}

urlpatterns = [

    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
    path('',include('firstsite.urls')),
    path('blog/',include('Blog.urls')),


    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', include('robots.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
    path('summernote/',include('django_summernote.urls')),
    path('captcha/', include('captcha.urls')),
    
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)