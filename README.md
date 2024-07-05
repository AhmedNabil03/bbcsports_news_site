<h1>Sports News Category Predictor</h1>
<p>This project is a web application that predicts the category of sports news articles using a Naive Bayes model. The application is built with Flask and uses a pre-trained TF-IDF vectorizer and a Naive Bayes model to classify the input text into one of the following sports categories:</p>
<ul>
    <li>Football</li>
    <li>Rugby</li>
    <li>Cricket</li>
    <li>Athletics</li>
    <li>Tennis</li>
</ul>
<h2>Table of Contents</h2>
<ul>
    <li><a href="#features">Features</a></li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#project-structure">Project Structure</a></li>
    <li><a href="#demo">Demo</a></li>
    <li><a href="#contributing">Contributing</a></li>
</ul>
<h2 id="features">Features</h2>
<ul>
    <li><strong>Text Preprocessing:</strong> The input text is cleaned and preprocessed to remove stop words, apply stemming, and standardize the text.</li>
    <li><strong>Prediction:</strong> Uses a pre-trained Naive Bayes model to predict the category of the sports news.</li>
    <li><strong>Responsive Design:</strong> The web interface is designed to be user-friendly and responsive.</li>
</ul>
<h2 id="installation">Installation</h2>
<p>To run this project locally, follow these steps:</p>
<ol>
    <li>Clone the repository</li>
    <li>Create a virtual environment</li>
    <li>Install the required packages (scikit-learn version used: 1.4.1post1)</li>
    <li>Run the application</li>
</ol>
<h2 id="usage">Usage</h2>
<ol>
    <li>Open your browser and go to <code>http://127.0.0.1:8080/</code>.</li>
    <li>Enter the sports news text in the text area.</li>
    <li>Click on the "Predict" button to see the predicted category of the sports news.</li>
</ol>
<h2 id="project-structure">Project Structure</h2>
<pre>
<code>
bbcsports_news_site/
├── app.py
├── requirements.txt
├── sport_model.pkl
├── sport_vectorizer.pkl
├── templates/
│   └── index.html
└── static/
    └── styles.css
</code>
</pre>
<ul>
    <li><strong>app.py:</strong> The main Flask application file that handles routing and prediction.</li>
    <li><strong>requirements.txt:</strong> The file that lists all Python dependencies.</li>
    <li><strong>sport_model.pkl:</strong> The pre-trained Naive Bayes model.</li>
    <li><strong>sport_vectorizer.pkl:</strong> The pre-trained TF-IDF vectorizer.</li>
    <li><strong>templates/:</strong> Contains the HTML file for the web interface.</li>
    <li><strong>static/:</strong> Contains the CSS file for styling the web interface.</li>
</ul>
<h2 id="demo">Demo</h2>
<p>You can see the application in action here: <a href="https://ahmednabil.pythonanywhere.com/">Sports News Category Predictor</a>. This is a temporary demo and might be unpublished in the future.</p>
<h2 id="contributing">Contributing</h2>
<p>Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or create a pull request.</p>
