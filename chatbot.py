import json
import random

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from utils.preprocessing import preprocess_text

# Load intents
with open('intents.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

patterns = []
tags = []

for intent in data['intents']:
    for pattern in intent['patterns']:
        patterns.append(preprocess_text(pattern))
        tags.append(intent['tag'])

# TF-IDF Vectorizer
vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(patterns)

def get_response(user_input):
    user_input = preprocess_text(user_input)

    user_vector = vectorizer.transform([user_input])

    similarity = cosine_similarity(user_vector, X)

    best_match_index = similarity.argmax()

    best_tag = tags[best_match_index]

    best_score = similarity[0][best_match_index]

    # Confidence threshold
    if best_score < 0.3:
        for intent in data['intents']:
            if intent['tag'] == 'fallback':
                return random.choice(intent['responses'])

    for intent in data['intents']:
        if intent['tag'] == best_tag:
            return random.choice(intent['responses'])

    return "I'm still learning! Try asking about machine learning or NLP."