from transformers import pipeline

# Load pre-trained sentiment analysis model
sentiment_model = pipeline("sentiment-analysis")

# Get user input
text = input("Enter a sentence for sentiment analysis: ")

# Predict sentiment
result = sentiment_model(text)[0]
print(f"🔍 Sentiment: {result['label']} (Confidence: {result['score']:.2f})")

