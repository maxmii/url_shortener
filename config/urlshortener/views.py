from django.shortcuts import render, redirect
from django.urls import reverse

from . import service
from .forms import URLShortenerForm


def index(request):
    url_form = URLShortenerForm()
    return render(request, 'main/index.html', {'form': url_form})


def shorten_post(request):
    return shorten(request, request.POST['original_url'])


def shorten(request, url):
    shortened_url_hash = service.shorten(url)
    shortened_url = request.build_absolute_uri(
        reverse('redirect', args=[shortened_url_hash])
    )

    return render(request, 'main/link.html', {'shortened_url': shortened_url})


def redirect_hash(request, url_hash):
    original_url = service.load_url(url_hash).original_url
    return redirect(original_url)
