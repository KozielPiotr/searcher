""""Views for search_app"""

from django.shortcuts import render


def home(request):
    """Home page for app and whole project"""
    return render(request, "base.html")


def new_search(request):
    """Processes user search"""
    search = request.POST.get("search")
    context = {
        "searched_phrase": search,
    }
    return render(request, "search_app/new_search.html", context=context)
