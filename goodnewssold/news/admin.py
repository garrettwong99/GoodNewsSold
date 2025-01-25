from django.contrib import admin
from .models import Source

@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    list_display = ('name', 'rss_url', 'added_on')  # Customize display