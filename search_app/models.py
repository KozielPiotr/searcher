# pylint: disable=too-few-public-methods
""""db models"""

from django.db import models


class Search(models.Model):
    """Stores phrases searched by users"""
    search = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.search)

    class Meta:
        """Giver plural form of class name"""
        verbose_name_plural = "Searches"
