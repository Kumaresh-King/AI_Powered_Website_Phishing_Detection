import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
from pathlib import Path
from urllib.parse import urlparse
import re

from model.feature_extraction import extract_features

app = Flask(__name__)
CORS(app)

# Load model
model_path = Path(__file__).resolve().parent.parent / "model" / "phishing_model.pkl"
model = joblib.load(model_path)

# Logs for dashboard
logs = []

# Trusted domains
TRUSTED_DOMAINS = [
    "google.com","github.com","whatsapp.com","youtube.com","linkedin.com",
    "microsoft.com","amazon.com","facebook.com","instagram.com","chatgpt.com"
]

# Suspicious TLDs
SUSPICIOUS_TLDS = ['.tk','.ml','.ga','.cf','.gq']

# Shorteners
SHORTENERS = ['bit.ly','tinyurl','goo.gl']


@app.route("/")
def home():
    return "AI Phishing Detection API Running 🚀"


@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json
        url = data["url"].lower()

        parsed = urlparse(url)
        domain = parsed.netloc

        # =========================
        # 1️⃣ WHITELIST CHECK
        # =========================
        if any(trusted in domain for trusted in TRUSTED_DOMAINS):
            return jsonify({
                "result": "legitimate",
                "confidence": 99.0,
                "source": "whitelist"
            })

        # =========================
        # 2️⃣ RULE-BASED DETECTION
        # =========================
        risk_score = 0

        if any(tld in domain for tld in SUSPICIOUS_TLDS):
            risk_score += 2

        if any(short in url for short in SHORTENERS):
            risk_score += 2

        if len(url) > 75:
            risk_score += 1

        if re.search(r'(?:\d{1,3}\.){3}\d{1,3}', url):
            risk_score += 3

        # =========================
        # 3️⃣ AI MODEL
        # =========================
        features = extract_features(url)
        proba = model.predict_proba([features])[0][1]

        # =========================
        # 4️⃣ FINAL DECISION LOGIC
        # =========================
        if risk_score >= 3:
            prediction = 1  # phishing
        else:
            prediction = 1 if proba > 0.75 else 0

        result = "phishing" if prediction == 1 else "legitimate"

        # Confidence
        if prediction == 1:
            confidence = proba
        else:
            confidence = 1 - proba

        confidence = float(round(confidence * 100, 2))

        # Save logs
        logs.append({
            "url": url,
            "result": result,
            "confidence": confidence,
            "risk_score": risk_score
        })

        return jsonify({
            "result": result,
            "confidence": confidence,
            "risk_score": risk_score,
            "source": "hybrid"
        })

    except Exception as e:
        return jsonify({"error": str(e)})


@app.route("/logs")
def get_logs():
    return jsonify(logs)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)