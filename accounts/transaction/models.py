from __future__ import unicode_literals
from django.db import models
from enumerify import fields

from .enums import AccountType


class Accounts(models.Model):
    label = models.CharField(max_length=64)
    type = fields.SelectIntegerField(blueprint=AccountType)

    class Meta:
        unique_together = (( 'label'),)
        verbose_name_plural = "accounts"

    def __unicode__(self):
        return self.get_name()

    def get_name(self):
        return u"#{}: {}".format(self.id, self.label)

