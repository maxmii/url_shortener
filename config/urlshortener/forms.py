from django.forms import ModelForm

from .models import Url


class URLShortenerForm(ModelForm):
    class Meta:
        model = Url
        exclude = ['hash', 'creation_date']
