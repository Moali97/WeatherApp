from django.db import models


class City(models.Model):
    name = models.CharField(max_length=25)

    class Meta:  # changes plural of city to cities instead of citys
        verbose_name_plural = 'cities'

    def __str__(self):
        return f"{self.name[:25]}..."