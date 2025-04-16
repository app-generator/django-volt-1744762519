# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Employee(models.Model):

    #__Employee_FIELDS__
    firstname = models.CharField(max_length=255, null=True, blank=True)
    midname = models.CharField(max_length=255, null=True, blank=True)
    lastname = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=255, null=True, blank=True)
    dob = models.DateTimeField(blank=True, null=True, default=timezone.now)
    age = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    address2 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    zip = models.CharField(max_length=255, null=True, blank=True)

    #__Employee_FIELDS__END

    class Meta:
        verbose_name        = _("Employee")
        verbose_name_plural = _("Employee")


class Department(models.Model):

    #__Department_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    note = models.CharField(max_length=255, null=True, blank=True)

    #__Department_FIELDS__END

    class Meta:
        verbose_name        = _("Department")
        verbose_name_plural = _("Department")


class Title(models.Model):

    #__Title_FIELDS__
    department = models.CharField(max_length=255, null=True, blank=True)

    #__Title_FIELDS__END

    class Meta:
        verbose_name        = _("Title")
        verbose_name_plural = _("Title")


class Status(models.Model):

    #__Status_FIELDS__
    description = models.CharField(max_length=255, null=True, blank=True)

    #__Status_FIELDS__END

    class Meta:
        verbose_name        = _("Status")
        verbose_name_plural = _("Status")


class Shift(models.Model):

    #__Shift_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)

    #__Shift_FIELDS__END

    class Meta:
        verbose_name        = _("Shift")
        verbose_name_plural = _("Shift")


class Gender(models.Model):

    #__Gender_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)

    #__Gender_FIELDS__END

    class Meta:
        verbose_name        = _("Gender")
        verbose_name_plural = _("Gender")



#__MODELS__END
