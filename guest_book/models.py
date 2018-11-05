import re

from django.db import models
from django.core import validators
from django.utils.translation import ugettext_lazy as _


uname_validator = [validators.RegexValidator(re.compile('^[\w.@+-]+$'),
                   _('Enter a valid username.'), _('invalid'))]


class CustomUser(models.Model):
    username = models.CharField(_('username'), max_length=45,
                                validators=uname_validator)
    email = models.EmailField(_('email address'), unique=True,
                              max_length=255)
    ip = models.GenericIPAddressField(null=True)
    browser = models.CharField(max_length=255, null=True)


class Message(models.Model):
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    link = models.URLField(blank=True)
    image = models.ImageField(upload_to='images/', blank=True)
