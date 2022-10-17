from django.db import models


class Marketplace(models.Model):
    name = models.CharField(max_length=100)
    active = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Marketplace"
        verbose_name_plural = "Marketplaces"

    def __str__(self):
        return self.name
