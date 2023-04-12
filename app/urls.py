from django.contrib import admin
from django.urls import path, include

from short_urls.views import UrlModelViewSet

from rest_framework import routers

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
]

router = routers.SimpleRouter()
router.register(r'short-urls', UrlModelViewSet)

urlpatterns += router.urls
