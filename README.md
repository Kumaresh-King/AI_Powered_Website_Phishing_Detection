# 🚀 AI-Powered Website Phishing Detection

A real-time phishing detection system integrated into a browser extension. The project uses machine learning to analyze URLs and identify suspicious websites before users can access them.

This solution combines:
- a browser extension for real-time monitoring,
- a Flask API for predictions,
- a trained phishing detection model,
- feature extraction logic for URL-based analysis.

It is designed to improve online security by detecting phishing attempts that often bypass traditional static blacklists.

## ✨ Features

- Real-time URL scanning while browsing
- AI-powered phishing detection using ML inference
- Browser extension integration for immediate warnings
- Automatic redirect to a warning page for detected phishing attempts
- Rule-based fallback logic for stronger detection signals
- Monitoring logs for analyzed URLs
- Lightweight, scalable architecture for browser-based security monitoring

## 🧠 How It Works

1. The user visits a website.
2. The browser extension captures the active tab URL.
3. The extension sends the URL to the backend API.
4. The backend extracts URL features.
5. The machine learning model predicts whether the website is phishing or legitimate.
6. If the result is phishing, the extension redirects the user to a warning page.

## 🛠️ Tech Stack

- Python
- Flask
- JavaScript
- Chrome Extension API
- HTML/CSS
- XGBoost / scikit-learn style ML pipeline
- Feature-based URL analysis

## 📁 Project Structure

```text
AI_Powered_Website_Phishing_Detection/
├── backend/
│   ├── api.py
│   └── requirements.txt
├── extension/
│   ├── background.js
│   ├── manifest.json
│   ├── popup.html
│   ├── warning.html
│   └── styles.css
├── model/
│   ├── feature_extraction.py
│   └── phishing_model.pkl
├── README.md
├── LICENSE
└── screenshots/
```

## ▶️ Local Setup

### 1) Clone the repository

```bash
git clone https://github.com/Kumaresh-King/AI_Powered_Website_Phishing_Detection.git
cd AI_Powered_Website_Phishing_Detection
```

### 2) Set up the backend

```bash
cd backend
pip install -r requirements.txt
python api.py
```

This starts the Flask API on a local port (default: 5000).

### 3) Load the browser extension in Chrome/Edge

1. Open `chrome://extensions` (or `edge://extensions`)
2. Turn on Developer Mode
3. Click Load unpacked
4. Select the `extension/` folder

### 4) Test the extension

- Visit a suspicious URL
- The extension will send the URL to the backend API
- If the URL is classified as phishing, the browser will redirect to the warning page

## ⚠️ Important Note for Local Testing

The extension currently calls a deployed Render URL:

```javascript
https://ai-powered-website-phishing-detection.onrender.com/predict
```

If you are running the API locally, update the request URL in `extension/background.js` to:

```javascript
http://localhost:5000/predict
```

This allows local testing without the deployed service.

## 🧪 Example API Request

```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"url":"https://login-secure-paypal-update.com"}'
```

Example response:

```json
{
  "result": "phishing",
  "confidence": 0.9
}
```

## 📊 Model and Feature Extraction

The project extracts meaningful URL-based signals such as:
- URL length
- domain length
- number of dots and special characters
- presence of IP addresses
- suspicious TLDs
- URL shorteners
- phishing-related keywords like login, secure, verify, bank, and account

These features are fed into the model to decide whether a site is phishing or legitimate.

## 🖼️ Demo / Screenshots

Add screenshots here to showcase the browser extension UI and warning page.

Example:

```markdown
![Extension popup](screenshots/extension-popup.png)
![Warning page](screenshots/warning-page.png)
```

## 📈 Future Improvements

- Improve the model with a larger phishing dataset
- Add more advanced URL-based and content-based features
- Support additional browsers
- Include a dashboard for analyzed URLs and detection statistics
- Add user override and allowlist functionality

## 🤝 Contributing

Contributions are welcome.

If you would like to contribute:
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a pull request

## 🧾 License

This project is licensed under the MIT License.

## 🔗 Repository

https://github.com/Kumaresh-King/AI_Powered_Website_Phishing_Detection
