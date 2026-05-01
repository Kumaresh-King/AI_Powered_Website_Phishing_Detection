from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import os
from pathlib import Path

# 🔧 Import your feature extractor
from model.feature_extraction import extract_features

app = Flask(__name__)
CORS(app)

# 📊 Logs storage
logs = []

# 📁 Load model safely
BASE_DIR = Path(__file__).resolve().parent.parent
model_path = BASE_DIR / "model" / "phishing_model.pkl"

if not model_path.exists():
    print("❌ Model file not found!")
    model = None
else:
    model = joblib.load(model_path)
    print("✅ Model loaded successfully")

# 🏠 Home route
@app.route("/")
def home():
    return "AI Phishing Detection API Running 🚀"

# 🔮 Prediction route
@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        if not data or "url" not in data:
            return jsonify({"error": "No URL provided"}), 400

        url = data["url"]

        # 🔍 Extract features (IMPORTANT: wrap in list)
        features = [extract_features(url)]

        if model:
            probs = model.predict_proba(features)[0]
            prediction = int(model.predict(features)[0])
            confidence = float(max(probs))
        else:
            # 🔥 fallback rule-based detection
            suspicious_words = ["login", "secure", "bank", "verify", "update"]
            if any(word in url.lower() for word in suspicious_words):
                prediction = 1
                confidence = 0.85
            else:
                prediction = 0
                confidence = 0.60

        result = "phishing" if prediction == 1 else "legitimate"

        # 📊 Store logs
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
        print("❌ Error:", str(e))
        return jsonify({"error": str(e)}), 500

# 📊 Logs route
@app.route("/logs", methods=["GET"])
def get_logs():
    return jsonify(logs)

# 🚀 Render-compatible server start
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)