from __future__ import unicode_literals

from django.db import models
# Create your models here.
from django.db.models.aggregates import Min


class Feature(models.Model):
    name = models.CharField(max_length=255, blank=False)
    tmc_alias = models.CharField(max_length=255, blank=False)
    file_mask = models.CharField(max_length=255, blank=False)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return str(self.name)


class Version(models.Model):
    name = models.CharField(max_length=255, blank=False)
    comment = models.CharField(max_length=255, blank=False)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class AutomationResult(models.Model):
    version = models.ForeignKey(Version, blank=False)
    feature = models.ForeignKey(Feature, blank=False)

    total = models.IntegerField(default=0)
    fail = models.IntegerField(default=0)

    start_time = models.DateTimeField()

    version_name = models.CharField(default=0, max_length=50)

    def __str__(self):
        return u"{} {}".format(self.version.name, self.feature.name)

    def passed(self):
        return self.total - (self.fail or 0)

    def link(self):
        return self.start_time or 'lol'


class FeatureMatching(models.Model):
    version = models.ForeignKey(Version, blank=False)
    feature = models.ManyToManyField(Feature, blank=False, verbose_name='Features')

    def __str__(self):
        return u"{}".format(self.version) or 'Unknown'


