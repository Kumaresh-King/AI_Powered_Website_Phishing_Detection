# 🚀 AI-Powered Phishing Detection Browser Extension

## 🔐 Overview
This project is a real-time phishing detection system integrated into a Chrome Extension. It uses Machine Learning (XGBoost) to analyze URLs and protect users from malicious websites.

---

## ✨ Features
- 🔍 Real-time URL scanning
- 🤖 AI-based phishing detection
- 🌐 Chrome Extension integration
- 🚫 Automatic phishing site blocking
- ⚠ Warning page with user override
- 📊 Dashboard for monitoring

---

## 🛠 Tech Stack
- Python (Flask)
- XGBoost (Machine Learning)
- JavaScript (Chrome Extension)
- HTML/CSS (UI)

---

## ⚙️ How It Works
1. User visits a website  
2. Extension captures URL  
3. Sends request to Flask API  
4. ML model predicts phishing risk  
5. If malicious → block & show warning  

---

## ▶️ How to Run Locally

### Backend
```bash
cd backend
pip install -r requirements.txt
python api.py