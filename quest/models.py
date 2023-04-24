from django.db import models


class Thing(models.Model):
    name = models.CharField(max_length=200)
    teaser = models.TextField(blank=True)
    slug = models.SlugField()
    description = models.TextField()
    poster = models.URLField(blank=True)
    illustration = models.URLField(blank=True)
    image = models.URLField(blank=True)
    caption = models.TextField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/thing/%s/' % self.slug

class Quest(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    active = models.BooleanField()
    description = models.TextField()
    threewords = models.CharField(max_length=100, blank=True, null=True)
    pluscode = models.CharField(max_length=100, blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    things = models.ManyToManyField(Thing)
    map = models.URLField(blank=True)

    class Meta:
        ordering = ['name','active']

    def __str__(self):
        return self.name
