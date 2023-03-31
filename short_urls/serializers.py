from rest_framework import serializers

from hashids import Hashids

from short_urls.models import Url


hashids = Hashids()


class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = ('id', 'long_url', 'short_url_hash', 'created')
        read_only_fields = ('id', 'short_url_hash', 'created')
    
    def create(self, validated_data):
        instance = super().create(validated_data)
        short_url_hash = hashids.encode(instance.pk)
        instance.short_url_hash = short_url_hash
        instance.save(update_fields=['short_url_hash'])
        return instance