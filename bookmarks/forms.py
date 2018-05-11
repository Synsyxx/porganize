from django import forms

from .models import Bookmark

class BookmarkForm(forms.ModelForm):
    """Form to create/edit bookmarks"""

    class Meta:
        model = Bookmark
        fields = ('url', 'name', 'notes')