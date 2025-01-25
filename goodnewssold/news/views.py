from django.shortcuts import render
from .models import Source

def home(request):
    """Display a list of news articles."""
    sources = Source.objects.all()  # Fetch all RSS feed sources
    return render(request, 'news/home.html', {'sources': sources})
