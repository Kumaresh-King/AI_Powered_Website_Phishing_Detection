from flask import Flask, app, request, jsonify
from flask_cors import CORS
import joblib
import os
import re
from urllib.parse import urlparse
from pathlib import Path

CORS(app, resources={r"/*": {"origins": "*"}})
# 📁 Load model safely
model_path = Path(__file__).resolve().parent.parent / "model" / "phishing_model.pkl"

if not model_path.exists():
    print("⚠ Model not found, running in fallback mode")
    model = None
else:
    model = joblib.load(model_path)

# 📊 Store logs
logs = []

# 🔍 Feature helpers
def has_ip(url):
    return 1 if re.search(r'(?:\d{1,3}\.){3}\d{1,3}', url) else 0

def extract_features(url):
    parsed = urlparse(url)

    return [[
        len(url),
        len(parsed.netloc),
        len(parsed.path),
        url.count('.'),
        url.count('-'),
        url.count('@'),
        url.count('?'),
        url.count('='),
        sum(c.isdigit() for c in url),
        sum(c.isalpha() for c in url),
        sum(not c.isalnum() for c in url),
        1 if parsed.scheme == "https" else 0,
        has_ip(url),
        parsed.netloc.count('.'),
        sum(word in url.lower() for word in ["login","secure","bank","verify","update"])
    ]]

# 🏠 Home route
@app.route("/")
def home():
    return "AI Phishing Detection API Running 🚀"

# 🔮 Prediction route
@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json
        url = data.get("url", "")

        features = extract_features(url)

        # If model not loaded, fallback logic
        if model:
            prediction = int(model.predict(features)[0])
            probs = model.predict_proba(features)[0]
            confidence = float(max(probs))   # highest probability
        else:
            # simple fallback rule
            prediction = 1 if "login" in url or "secure" in url else 0
            confidence = 0.6

        result = "phishing" if prediction == 1 else "legitimate"

        logs.append({
            "url": url,
            "result": result,
            "confidence": confidence
        })

        return jsonify({
            "result": result,
            "confidence": confidence
        })

    except Exception as e:
        return jsonify({"error": str(e)})

# 📊 Logs route
@app.route("/logs", methods=["GET"])
def get_logs():
    return jsonify(logs)

# 🚀 Render-compatible start
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)