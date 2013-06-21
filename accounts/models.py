from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

from userena.managers import ASSIGNED_PERMISSIONS
from guardian.shortcuts import assign
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


def create_profile(user=None, profile=None, *args, **kwargs):
    """
    Create user profile if necessary
    """
    if profile:
        return { 'profile': profile }
    if not user:
        return
    return { 'profile': Profile.objects.get_or_create(user=user)[0] }


def set_guardian_permissions(user=None, profile=None, *args, **kwargs):
    """
    Give the user permission to modify themselves
    """
    if not user or not user.is_authenticated():
        return
    if profile:
        # Give permissions to view and change profile
        for perm in ASSIGNED_PERMISSIONS['profile']:
            assign(perm[0], user, profile)

    # Give permissions to view and change itself
    for perm in ASSIGNED_PERMISSIONS['user']:
        assign(perm[0], user, user)
