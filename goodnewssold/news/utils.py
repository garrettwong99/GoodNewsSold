import feedparser

def fetch_rss_feed(url):
    """Fetch and parse the RSS feed from the given URL."""
    feed = feedparser.parse(url)
    return feed  # Contains feed entries and metadata