import feedparser
from django.shortcuts import render
from .models import Source
from .analysis import analyze_sentiment  # Import the sentiment analysis function

def home(request):
    """Display a list of news articles."""
    sources = Source.objects.all()  # Fetch all RSS feed sources

    articles = []
    for source in sources:
        feed = feedparser.parse(source.rss_url)
        for entry in feed.entries:
            sentiment = analyze_sentiment(entry.title)
            articles.append({
                'title': entry.title,
                'link': entry.link,
                'sentiment': sentiment['compound']  # Use the compound score for ranking
            })
    
    # Sort articles by sentiment score in descending order and select the top 50
    articles = sorted(articles, key=lambda x: x['sentiment'], reverse=True)[:50]
    
    context = {
        'articles': articles
    }
    return render(request, 'news/home.html', context)