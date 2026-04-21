import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
import joblib

from feature_extraction import extract_features

# Load dataset
df = pd.read_csv("../dataset/url.csv")

# Ensure correct columns
# url column and label column (0 = legit, 1 = phishing)

X = df['url'].apply(lambda url: extract_features(url)).tolist()
y = df['label']

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = XGBClassifier(
    use_label_encoder=False,
    eval_metric='logloss'
)

model.fit(X_train, y_train)

# Accuracy
accuracy = model.score(X_test, y_test)
print("Model Accuracy:", accuracy)

# Save model
joblib.dump(model, "phishing_model.pkl")

print("Model saved successfully!")