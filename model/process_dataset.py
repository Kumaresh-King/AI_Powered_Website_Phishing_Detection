import pandas as pd
from feature_extraction import extract_features

# Load raw dataset
df = pd.read_csv("../dataset/url.csv")  # columns: url, label

# Apply feature extraction
feature_data = df["url"].apply(extract_features)

# Convert to dataframe
X = pd.DataFrame(feature_data.tolist())

# Add label
X["label"] = df["label"]

# Save processed dataset
X.to_csv("../dataset/processed_urls.csv", index=False)

print("✅ Dataset processed and saved!")