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
    return filename
        
class ServiceBadge(models.Model):
    description = models.CharField(max_length=255)
    picture = models.ImageField(upload_to=badge_upload, null=True, blank=True)
 
    def __unicode__(self):
        return self.description

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

    badges = models.ManyToManyField(ServiceBadge)

    def __unicode__(self):
        return self.name



    
    