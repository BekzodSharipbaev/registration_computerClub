from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import EmailValidator

from .validators import validate_password, validate_age, validate_positive_number, validate_username, validate_phone_number

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200, verbose_name=_("name"))
    username = models.CharField(max_length=200, verbose_name=_("username"), validators=[validate_username])
    email = models.EmailField(unique=True, verbose_name=_("email"), validators=[EmailValidator()])
    password = models.CharField(max_length=100, verbose_name=_("password"), validators=[validate_password])
    phone_number = models.PositiveSmallIntegerField(verbose_name=_("phone number"), validators=[validate_phone_number, validate_positive_number])
    age = models.PositiveSmallIntegerField(verbose_name=_("age"), validators=[validate_age, validate_positive_number])
    experience = models.PositiveSmallIntegerField(verbose_name=_("experience"), validators=[validate_positive_number])
    OPERATING_SYSTEMS = (
        ['Wndws', 'Windows'],
        ['Lnx', 'Linux'],
        ['MO', 'MacOS'],
    )
    operating_system = models.CharField(choices=OPERATING_SYSTEMS,max_length=200, verbose_name=_("operating system"))
    programs = models.CharField(max_length=200, verbose_name=_("programs"))
    comp_games = models.CharField(max_length=200, verbose_name=_("computer games"))
    COMP_HARDWARES = (
        ['PC', _('Personal Computer')],
        ['LP', _('Laptop')],
    )
    comp_hardware = models.CharField(choices=COMP_HARDWARES, max_length=100, verbose_name=_("computer hardware"))
    RECOMMENDERS = (
        ['inst', 'Instagram'],
        ['TT', 'TikTok'],
        ['WS', _('Web Sites')],
        ['O', _('Other')],
    )
    sources = models.CharField(choices=RECOMMENDERS, max_length=100, verbose_name=_("sources"))
    profession = models.CharField(max_length=250, verbose_name=_("profession"))
    target = models.CharField(max_length=250, verbose_name=_("target"))
    ideas = models.TextField(blank=True, null=True, verbose_name=_("ideas"))
    
    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def __str__(self):
        return f"{self.pk})  {self.name} - {self.age}"
    
