from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.urls import path, re_path, include
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from django.contrib import admin
from django.urls import path,include,re_path
from rest_framework_swagger.views import get_swagger_view  # <-- Here
schema_view = get_swagger_view(title='Swagger API')
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .api import api_router

schema_view = get_schema_view(
    openapi.Info(
        title="Swagger API",
        default_version='v1',
        description="Welcome to the world of Swagger API",
        # terms_of_service="https://www.jaseci.org",
        # contact=openapi.Contact(email="jason@jaseci.org"),
        # license=openapi.License(name="Awesome IP"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
# ends here
urlpatterns = [
    re_path(r'^doc(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),  #<-- Here
    path('mytaxboard_api', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),  #<-- Here
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),  #<-- Here
    path('admin/', (admin.site.urls)),
    path('',include('home.urls')),
    path('',include('business.urls')),
    # path('mytaxboard',include('mytaxboard_api.urls')),
    path('account/',include('account.urls')),
    # path('main_app/',include('main_app.urls')),
    path('cms/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),
    path('pages/', include(wagtail_urls)),
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = urlpatterns + [
    path("blog", include(wagtail_urls)),
]

handler500 = 'home.views.handler500'
handler403 = 'home.views.handler403'
handler404 = 'home.views.handler404'