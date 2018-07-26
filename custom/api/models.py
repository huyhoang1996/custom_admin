from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Notification(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    publish = models.BooleanField(default=False)
    users = models.ManyToManyField('UserIntermediate', related_name='notification_users')


    def __str__(self):
        return '%s' % (self.name)


class UserIntermediate(models.Model):
    user = models.ForeignKey(User, related_name='user')
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return '%s' % (self.user.email)