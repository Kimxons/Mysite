from __future__ import unicode_literals

from django.db import models

class Hello(models.Model):
    #portfolio models
    title = models.CharField(max_length=120)
    desc = models.TextField()
    url = models.URLField(max_length=120)
    slug = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    img_name = models.CharField(max_length=120)

    def __str__(self):
        return self.title