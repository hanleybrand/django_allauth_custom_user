# coding=utf-8
import sys

from django.db import models
from django.db.models.signals import post_syncdb
from django.contrib.sites.models import Site
from django.conf import settings
from django.contrib.auth.models import AbstractUser

from allauth.socialaccount.providers import registry
from allauth.socialaccount.models import SocialApp
from allauth.socialaccount.providers.oauth.provider import OAuthProvider
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider


# you can simply subclass django.contrib.auth.models.AbstractUser
# and add your custom profile fields.
# This class provides the full implementation of the default User as an abstract model.
class CustomUser(AbstractUser):
    GENDER_CHOICES = (('', 'Prefer not to say'), ('F', 'Female'), ('M', 'Male'), ('O', 'Other'),)
    date_of_birth = models.DateField(help_text='YYYY-MM-DD format')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)


def setup_dummy_social_apps(sender, **kwargs):
    """
    `allauth` needs tokens for OAuth based providers. So let's
    setup some dummy tokens
    """
    site = Site.objects.get_current()
    for provider in registry.get_list():
        if (isinstance(provider, OAuth2Provider)
            or isinstance(provider, OAuthProvider)):
            try:
                SocialApp.objects.get(provider=provider.id,
                                      sites=site)
            except SocialApp.DoesNotExist:
                print ("Installing dummy application credentials for %s."
                       " Authentication via this provider will not work"
                       " until you configure proper credentials via the"
                       " Django admin (`SocialApp` models)" % provider.id)
                app = SocialApp.objects.create(provider=provider.id,
                                               secret='secret',
                                               client_id='client-id',
                                               name='Dummy %s app' % provider.id)
                app.sites.add(site)


# We don't want to interfere with unittests et al
if 'syncdb' in sys.argv:
    post_syncdb.connect(setup_dummy_social_apps, sender=sys.modules[__name__])