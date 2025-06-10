import nltk
from nltk.corpus import movie_reviews
import random
import joblib
import os
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

nltk.download('movie_reviews')

documents = [(movie_reviews.raw(fileid), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]
random.shuffle(documents)

texts, labels = zip(*documents)

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    return text

cleaned_texts = [clean_text(t) for t in texts]

pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(stop_words='english', max_features=5000)),
    ('clf', LogisticRegression(max_iter=1000))
])

pipeline.fit(cleaned_texts, labels)

model_dir = os.path.join(os.path.dirname(__file__), '..', 'model')
os.makedirs(model_dir, exist_ok=True)
joblib.dump(pipeline, os.path.join(model_dir, 'sentiment_model.pkl'))

print("✅ Model trained and saved successfully.")
