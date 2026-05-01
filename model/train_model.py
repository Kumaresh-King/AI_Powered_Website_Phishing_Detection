import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# 📁 Load processed dataset
# Make sure this file exists in: AIPWPD/dataset/processed_url.csv
df = pd.read_csv("../dataset/processed_urls.csv")

# 🚨 IMPORTANT: last column must be 'label'
if "label" not in df.columns:
    raise Exception("❌ 'label' column not found in dataset")

# 🔹 Split features & target
X = df.drop("label", axis=1)
y = df["label"]

# 🔀 Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 🌲 Train model (strong + stable)
model = RandomForestClassifier(
    n_estimators=200,
    max_depth=15,
    random_state=42
)

model.fit(X_train, y_train)

# 📊 Evaluate
accuracy = model.score(X_test, y_test)
print(f"✅ Model Accuracy: {accuracy * 100:.2f}%")

# 💾 Save model
joblib.dump(model, "../model/phishing_model.pkl")

print("🚀 Model trained and saved successfully!")