from django.db import models
from django.urls import reverse


class Img(models.Model):
    img = models.ImageField()
    description = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-id']

    def get_absolute_url(self):
        return reverse('img-detail', args=[str(self.id)])
