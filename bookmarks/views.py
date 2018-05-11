from django.shortcuts import render
from .models import Bookmark, PersonalBookmark

def index(request):
    context = {}
    # TODO: business logic, get data, etc.
    context['bookmarks'] = Bookmark.objects.all()
    if request.user.is_anonymous:
        context['personal_bookmarks'] = PersonalBookmark.objects.none()
    else:
        context['personal_bookmarks'] = PersonalBookmark.objects.filter(user=request.user)
    return render(request, 'bookmarks/index.html', context)
