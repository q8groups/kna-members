from django.db import models

# Create your models here.
class member(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/members/')

    def __unicode__(self):
        return self.name


class ministers(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/ministres/')

    def __unicode__(self):
        return self.name
