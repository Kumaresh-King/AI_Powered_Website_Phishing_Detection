import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from feature_extraction import extract_features

# 📁 Load dataset
df = pd.read_csv("../dataset/url.csv")

# ✅ Make sure columns: url, label
X = df["url"].apply(extract_features).tolist()
y = df["label"]

# 🔀 Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 🌲 Strong model
model = RandomForestClassifier(
    n_estimators=200,
    max_depth=15,
    random_state=42
)

model.fit(X_train, y_train)

# 📊 Accuracy
accuracy = model.score(X_test, y_test)
print("Accuracy:", accuracy)

# 💾 Save model
joblib.dump(model, "../model/phishing_model.pkl")

print("Model trained and saved ✅")