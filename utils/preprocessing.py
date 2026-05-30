import nltk
import string

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download NLTK resources
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

def preprocess_text(text):

    text = text.lower().strip()

    tokens = word_tokenize(text)

    cleaned_tokens = []

    for word in tokens:

        if word not in stop_words and word not in string.punctuation:

            lemma = lemmatizer.lemmatize(word)

            cleaned_tokens.append(lemma)

    return " ".join(cleaned_tokens)