from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

addressType = (
    ("HOME","HOME"),
    ("OFFICE","OFFICE"),
    ("OTHER","OTHER")
)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class profile(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    profile_id = models.CharField(primary_key=True,max_length=100)
    first_name  = models.CharField(max_length=100,default='',null=True)
    last_name = models.CharField(max_length=100,default='',null=True)
    business_name = models.CharField(max_length=100,default='',null=True)
    gst = models.CharField(max_length=100,default='',null=True)
    email = models.CharField(max_length=100, default='', null=True)
    mobile = models.CharField(max_length=100, default='', null=True)
    password = models.CharField(max_length=100,default='', null=True)
    is_verified_email = models.BooleanField(default=False)
    is_verified_mobile = models.BooleanField(default=False)
    otp = models.CharField(max_length=6, null=True, blank=True)

    def __str__(self):
        return self.profile_id


class profile_address(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    address_id = models.CharField(primary_key=True, max_length=100)
    address_type = models.CharField(max_length=10,choices=addressType,default='HOME')
    address_nickname = models.CharField(max_length=100,null=True,default='')
    address = models.CharField(max_length=100,default='',null=True)

    def __str__(self):
        return self.address_id


class profile_views(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    view_id = models.CharField(primary_key=True,max_length=100)
    view_description = models.TextField(max_length=1000,null=True,default=dict)
    view_count = models.CharField(max_length=100,null=True,default='')

    def __str__(self):
        return self.view_id