from django.db import models


class City(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    # changes plural of city to cities instead of citys
    class Meta:
        verbose_name_plural = 'cities'
