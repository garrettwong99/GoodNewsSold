import feedparser
from django.shortcuts import render
from .models import Source

def home(request):
    """Display a list of news articles."""
    sources = Source.objects.all()  # Fetch all RSS feed sources

    articles = []
    for source in sources:
        feed = feedparser.parse(source.rss_url)
        for entry in feed.entries:
            articles.append({
                'title': entry.title,
                'link': entry.link,
            })
    
    context = {
        'articles': articles
    }
    return render(request, 'news/home.html', context)