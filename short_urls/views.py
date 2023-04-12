from short_urls.models import Url
from short_urls.serializers import UrlSerializer

from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import permissions


class UrlModelViewSet(mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):
    
    serializer_class = UrlSerializer
    queryset = Url.objects.all()
    lookup_field = 'short_url_hash'

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    
    def get_permissions(self):
        if self.action == 'destroy':
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]