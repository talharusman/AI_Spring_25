import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import LabelEncoder

# 1. Simulate a sample dataset
data = {
    'word_freq_offer': [0.1, 0.9, 0.05, 0.3, 0.7, 0.02],
    'word_freq_free': [0.2, 0.8, 0.1, 0.1, 0.6, 0.01],
    'email_length': [100, 400, 90, 300, 350, 80],
    'has_link': [1, 1, 0, 1, 1, 0],
    'sender': ['marketing@promo.com', 'scam@spam.net', 'friend@mail.com', 'newsletter@deals.com', 'spammy@bad.com', 'team@work.com'],
    'label': [1, 1, 0, 1, 1, 0]
}

df = pd.DataFrame(data)

# 2. Preprocess sender (categorical feature) using Label Encoding
label_encoder = LabelEncoder()
df['sender_encoded'] = label_encoder.fit_transform(df['sender'])

# 3. Prepare features and label
features = df[['word_freq_offer', 'word_freq_free', 'email_length', 'has_link', 'sender_encoded']]
labels = df['label']

# 4. Split data
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.33, random_state=42)

# 5. Train model (Logistic Regression)
model = LogisticRegression()
model.fit(X_train, y_train)

# 6. Predict and evaluate
y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

# 7. Deploy model to predict a new email
new_email = pd.DataFrame({
    'word_freq_offer': [0.6],
    'word_freq_free': [0.7],
    'email_length': [320],
    'has_link': [1],
    'sender': ['scam@spam.net']
})

# Encode the new sender
new_email['sender_encoded'] = label_encoder.transform(new_email['sender'])
new_features = new_email[['word_freq_offer', 'word_freq_free', 'email_length', 'has_link', 'sender_encoded']]

# Predict
prediction = model.predict(new_features)
print("\nSpam Prediction (1=spam, 0=not spam):", prediction[0])
