import random
import string
from django.utils import timezone

from .models import Url


def shorten(url):
    random_hash = ''.join(
        random.choice(
            string.ascii_uppercase + string.digits + string.ascii_lowercase
        )
        for _ in range(7)
    )

    url_mapping = Url(
        original_url=url, hash=random_hash, creation_date=timezone.now()
    )

    url_mapping.save()

    return random_hash


def load_url(url_hash):
    return Url.objects.get(hash=url_hash)
