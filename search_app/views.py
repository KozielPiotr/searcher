""""Views for search_app"""

from bs4 import BeautifulSoup
import requests
from requests.utils import requote_uri
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Search


BASE_CRAIGLIST_URL = "https://warsaw.craigslist.org/search/?query={}"
BASE_IMAGE_URL = 'https://images.craigslist.org/{}_300x300.jpg'


def home(request):
    """Home page for app and whole project"""
    return render(request, "base.html")


def new_search(request):
    """Processes user search"""
    search = request.POST.get("search")
    try:
        Search.objects.create(search=search)
    except IntegrityError:
        return HttpResponseRedirect(reverse("search_app:home"))
    final_url = BASE_CRAIGLIST_URL.format(requote_uri(search))
    data = requests.get(final_url).text
    soup = BeautifulSoup(data, features="html.parser")
    posts_list = soup.find_all("li", {"class": "result-row"})
    final_posts = []

    for post in posts_list:
        post_title = post.find(class_='result-title').text
        post_url = post.find('a').get('href')

        if post.find(class_='result-price'):
            post_price = post.find(class_='result-price').text
        else:
            post_price = 'N/A'

        if post.find(class_='result-image').get('data-ids'):
            post_image_id = post.find(class_='result-image').get('data-ids').split(',')[0].split(':')[1]
            post_image_url = BASE_IMAGE_URL.format(post_image_id)
            print(post_image_url)
        else:
            post_image_url = 'https://craigslist.org/images/peace.jpg'

        final_posts.append((post_title, post_url, post_price, post_image_url))

    context = {
        "searched_phrase": search,
        "posts": final_posts
    }
    return render(request, "search_app/new_search.html", context=context)
