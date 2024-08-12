import pickle
import re 
from pathlib import Path
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

BASE_DIR = Path(__file__).resolve(strict=True).parent

with open(f"{BASE_DIR}/pipeline_incident_report.pkl", "rb") as f:
    model = pickle.load(f)



def work(text):
    nltk.download('stopwords')
    nltk.download('punkt')
    nltk.download('wordnet')
    stop_words = set(stopwords.words('french'))    
    lemmatizer = WordNetLemmatizer()

    text = text.lower()  # Convert to lowercase
    text = re.sub(r'\d+', '', text)  # Remove numbers
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    tokens = word_tokenize(text)  # Tokenize text
    filtered_tokens = [word for word in tokens if word not in stop_words]  # Remove stop words
    lemmatized_tokens = [lemmatizer.lemmatize(word) for word in filtered_tokens]
    preprocessed_txt = ' '.join(lemmatized_tokens)

    pred = model.predict([preprocessed_txt])
    return pred