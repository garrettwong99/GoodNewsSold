import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download the VADER lexicon
nltk.download('vader_lexicon')

# Initialize the VADER sentiment intensity analyzer
sid = SentimentIntensityAnalyzer()

# Define custom phrases to favor or dislike
FAVOR_PHRASES = ['dog', 'family', 'stranger']
DISLIKE_PHRASES = ['horoscope']

def analyze_sentiment(text):
    scores = sid.polarity_scores(text)
    
    # Adjust scores based on custom phrases
    for phrase in FAVOR_PHRASES:
        if phrase in text.lower():
            scores['compound'] += 0.2  # Increase the compound score for favored phrases
    
    for phrase in DISLIKE_PHRASES:
        if phrase in text.lower():
            scores['compound'] -= 0.2  # Decrease the compound score for disliked phrases
    
    return scores