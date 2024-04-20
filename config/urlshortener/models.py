from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Url(models.Model):

    class URLShortenerAPIChoices(models.TextChoices):
        ADFLY = 'Ad', _('Adf.ly')
        BITLY = 'Bi', _('Bit.ly')
        CHILPIT = 'Ch', _('Chilp.it')
        CLCKRU = 'Cl', _('Clck.ru')
        CUTTLY = 'Cu', _('Cutt.ly')
        DAGD = 'Da', _('Da.gd')
        GITIO = 'Gi', _('Git.io')
        ISGD = 'Is', _('Is.gd')
        OSDB = 'Os', _('Os.db')
        OWLY = 'Ow', _('Ow.ly')
        POST = 'Po', _('Po.st')
        TINYURL = 'Ti', _('TinyURL.com')
        QPSRU = 'Qp', _('Qps.ru')

    original_url = models.URLField(max_length=256)
    hash = models.CharField(max_length=10)
    creation_date = models.DateTimeField('creation date')
    api_choice = models.CharField(
        max_length=2,
        choices=URLShortenerAPIChoices.choices,
        default=URLShortenerAPIChoices.TINYURL,
    )
