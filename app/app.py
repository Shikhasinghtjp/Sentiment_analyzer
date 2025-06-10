from flask import Flask, request, render_template
import joblib
import re
import os

app = Flask(__name__)

# Load the model
model_path = os.path.join(os.path.dirname(__file__), '..', 'model', 'sentiment_model.pkl')
model = joblib.load(model_path)

# Simple text cleaning
def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    return text

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        text = request.form.get('text', '').strip()
        if not text:
            raise ValueError("Input text cannot be empty.")
        cleaned = clean_text(text)
        prediction = model.predict([cleaned])[0]
        sentiment = "Positive 😄" if prediction == "pos" else "Negative ☹️"
        return render_template("index.html", prediction=f"Sentiment: {sentiment}", sentiment_label=prediction)
    except Exception as e:
        return render_template("index.html", error=f"{str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
