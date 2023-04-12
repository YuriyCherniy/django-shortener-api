from django.db import models
from django.contrib.auth import get_user_model


class Url(models.Model):
    long_url = models.URLField(max_length=2048)
    short_url_hash = models.CharField(max_length=50)
    user = models.ForeignKey(
        get_user_model(), null=True, blank=True, on_delete=models.CASCADE
        )
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'[ {self.long_url[:40]} ] created at [{self.created}]'
