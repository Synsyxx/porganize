from django.shortcuts import render
from .models import Bookmark

def index(request):
    context = {}
    # TODO: business logic, get data, etc.
    context['bookmarks'] = Bookmark.objects.all()
    return render(request, 'bookmarks/index.html', context)
