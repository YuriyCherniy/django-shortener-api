from rest_framework import generics

from short_urls.models import Url
from short_urls.serializers import UrlSerializer


class UrlCreate(generics.CreateAPIView):
    serializer_class = UrlSerializer


class UrlRetrive(generics.RetrieveAPIView):
    serializer_class = UrlSerializer
    queryset = Url.objects.all()
    lookup_field = 'short_url_hash'