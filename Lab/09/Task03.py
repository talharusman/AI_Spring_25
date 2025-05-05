import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# 1. Simulate the dataset
data = {
    'spending_last_6_months': [1200, 300, 5000, 700, 8000, 200, 3500, 400, 9000, 600],
    'age': [25, 45, 32, 36, 29, 60, 40, 55, 28, 50],
    'num_visits': [10, 5, 25, 6, 30, 3, 18, 4, 33, 7],
    'purchase_frequency': [5, 1, 10, 2, 12, 1, 7, 2, 15, 3],
    'label': [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]  # 1 = high-value, 0 = low-value
}
df = pd.DataFrame(data)

# 2. Handle missing values (none here, but check anyway)
print("Missing values:\n", df.isnull().sum())

# 3. Feature Scaling
scaler = StandardScaler()
features = df[['spending_last_6_months', 'age', 'num_visits', 'purchase_frequency']]
features_scaled = scaler.fit_transform(features)
labels = df['label']

# 4. Split data
X_train, X_test, y_train, y_test = train_test_split(features_scaled, labels, test_size=0.3, random_state=42)

# 5. Train an SVM model (Linear Kernel)
svm = SVC(kernel='linear')
svm.fit(X_train, y_train)

# 6. Predict
y_pred = svm.predict(X_test)

# 7. Evaluate the model
print("\nAccuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

# 8. Extract separating hyperplane (decision rule)
coef = svm.coef_[0]
intercept = svm.intercept_[0]
feature_names = features.columns

print("\nSeparating Hyperplane Equation:")
equation = " + ".join([f"{round(coef[i], 3)} * {feature_names[i]}" for i in range(len(coef))])
print(f"{equation} + {round(intercept, 3)} = 0")

# 9. Rule example (manual logic)
print("\nSimple Rule of Thumb:")
print("If the weighted combination of features exceeds the threshold, classify as high-value (1), else low-value (0).")
