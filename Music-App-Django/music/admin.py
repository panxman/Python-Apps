from django.contrib import admin
from .models import Album, Song


class SongInLine(admin.TabularInline):
    model = Song
    extra = 3


class AlbumAdmin(admin.ModelAdmin):
    inlines = [SongInLine]
    list_display = ('artist', 'album_title', 'genre')
    list_filter = ['artist']


admin.site.register(Album, AlbumAdmin)
