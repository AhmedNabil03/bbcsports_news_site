import os
from flask import Flask, render_template, request
import pickle
import pandas as pd
import re

# import nltk
# nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer

from sklearn.feature_extraction.text import TfidfVectorizer

app = Flask(__name__)

# Define paths to models
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'sport_model.pkl')
VECTORIZER_PATH = os.path.join(os.path.dirname(__file__), 'sport_vectorizer.pkl')

# Load the model and vectorizer
with open(MODEL_PATH, 'rb') as model_file:
    model = pickle.load(model_file)

with open(VECTORIZER_PATH, 'rb') as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

# Preprocessing function
stop_words = set(stopwords.words('english'))
stemmer = SnowballStemmer('english')

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[0-9]', '', text)
    text = ' '.join([word for word in text.split() if word not in stop_words and len(word) > 1])
    text = re.sub(r'\s+', ' ', text).strip()
    text = ' '.join([stemmer.stem(word) for word in text.split()])
    return text

label_map_reverse = {0: 'football', 1: 'rugby', 2: 'cricket', 3: 'athletics', 4: 'tennis'}

def predict_sport_category(text):
    processed_text = preprocess_text(text)
    text_series = pd.Series([processed_text])
    text_vectorized = vectorizer.transform(text_series)
    prediction = model.predict(text_vectorized)[0]
    predicted_sport = label_map_reverse[prediction]
    return predicted_sport

# Route for home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        news_text = request.form['news']
        prediction = predict_sport_category(news_text)
        return render_template('index.html', prediction=prediction, news=news_text)

if __name__ == '__main__':
    app.run(debug=False, port=8080)
