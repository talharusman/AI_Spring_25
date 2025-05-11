import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error, r2_score

# 1. Simulate the dataset
data = {
    'square_feet': [1500, 2000, 1700, 2500, 1400, 3000],
    'bedrooms': [3, 4, 3, 5, 2, 4],
    'bathrooms': [2, 3, 2, 4, 1, 3],
    'age': [10, 5, 8, 3, 20, 2],
    'neighborhood': ['A', 'B', 'A', 'C', 'A', 'B'],
    'price': [300000, 500000, 350000, 600000, 280000, 520000]
}
df = pd.DataFrame(data)

# 2. Check and handle missing values (none in this example)
print("Missing values:\n", df.isnull().sum())

# 3. Separate features and target
X = df.drop('price', axis=1)
y = df['price']

# 4. One-hot encode the categorical 'neighborhood' column
categorical_features = ['neighborhood']
numeric_features = ['square_feet', 'bedrooms', 'bathrooms', 'age']

preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(), categorical_features)
    ],
    remainder='passthrough'  # keep numeric columns as is
)

# 5. Create a pipeline with preprocessing and regression model
pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('model', LinearRegression())
])

# 6. Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 7. Fit model
pipeline.fit(X_train, y_train)

# 8. Predict and evaluate
y_pred = pipeline.predict(X_test)
print("\nPredictions on test data:", y_pred)

# Evaluation
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print("Mean Squared Error:", mse)
print("R² Score:", r2)

# 9. Predict the price of a new house
new_house = pd.DataFrame({
    'square_feet': [1800],
    'bedrooms': [3],
    'bathrooms': [2],
    'age': [6],
    'neighborhood': ['B']
})
predicted_price = pipeline.predict(new_house)
print("\nPredicted price for new house:", predicted_price[0])


