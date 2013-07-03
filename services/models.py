import os
from django.db import models

# Create your models here.
class ServiceCategory(models.Model):
    """
    A Category such as "Hosting, Food, ..."
    """
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

def badge_upload(instance, filename):
    return os.path.join("badges", filename)

def badgecat_upload(instance, filename):
    return os.path.join("badgecats", filename)

class ServiceBadgeCategory(models.Model):
    """
    A category for the badges
    """
    name = models.CharField(max_length=255)
    picture = models.ImageField(upload_to=badgecat_upload, null=True, blank=True)
    
    def __unicode__(self):
        return self.name
    
    
class ServiceBadge(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=255)
    picture = models.ImageField(upload_to=badge_upload, null=True, blank=True)
    category = models.ForeignKey(ServiceBadgeCategory)
 
    def __unicode__(self):
        return u"%s (%s)" % (self.name, self.description)

class Service(models.Model):
    """
    A service such as CouchSurfing, AirBNB, ...
    """
    class Meta:
        ordering = ('category',)
    
    name = models.CharField(max_length=255)
    description = models.TextField()
    website = models.URLField()
    logo_url = models.URLField()
    profile_url_template = models.CharField(max_length=255)

    category = models.ForeignKey(ServiceCategory, related_name='services')

    badges = models.ManyToManyField(ServiceBadge, related_name='services')

    def __unicode__(self):
        return self.name



    
    