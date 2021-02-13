from django.contrib import admin

from pictures.models import Picture


@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    list_display = ('pk', 'created', 'width', 'height')
    search_fields = ('pk', 'created')
    list_filter = ('created',)
