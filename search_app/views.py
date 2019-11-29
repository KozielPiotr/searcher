""""Views for search_app"""

from django.shortcuts import render


def home(request):
    return render(request, "base.html")
