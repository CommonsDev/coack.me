from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

from userena.models import UserenaBaseProfile

from services.models import Service

    
class Profile(UserenaBaseProfile):
    user = models.OneToOneField(User,
                                unique=True,
                                verbose_name=_('user'),
                                related_name='profile')
    
    services = models.ManyToManyField(Service,
                                      through='UserService')

class UserService(models.Model):
    """
    Link a user to a service and stores his username
    """
    profile = models.ForeignKey(Profile, related_name='service_detailed')
    service = models.ForeignKey(Service)
    username = models.CharField(max_length=255)
