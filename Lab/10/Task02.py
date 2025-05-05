import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler, LabelEncoder
import matplotlib.pyplot as plt
import seaborn as sns

# Sample vehicle data
data = {
    'vehicle_serial_no': [5, 3, 8, 2, 4, 7, 6, 10, 1, 9],
    'mileage': [150000, 120000, 250000, 80000, 100000, 220000, 180000, 300000, 75000, 280000],
    'fuel_efficiency': [15, 18, 10, 22, 20, 12, 16, 8, 24, 9],
    'maintenance_cost': [5000, 4000, 7000, 2000, 3000, 6500, 5500, 8000, 1500, 7500],
    'vehicle_type': ['SUV', 'Sedan', 'Truck', 'Hatchback', 'Sedan', 'Truck', 'SUV', 'Truck', 'Hatchback', 'SUV']
}

# Create DataFrame
df = pd.DataFrame(data)

# Encode categorical 'vehicle_type' into numeric values
le = LabelEncoder()
df['vehicle_type_encoded'] = le.fit_transform(df['vehicle_type'])

# Features for clustering (excluding serial number)
features = ['mileage', 'fuel_efficiency', 'maintenance_cost', 'vehicle_type_encoded']
X = df[features]

# ----------------- Clustering Without Scaling ----------------- #
kmeans_no_scaling = KMeans(n_clusters=3, random_state=0)
df['cluster_no_scaling'] = kmeans_no_scaling.fit_predict(X)

# ----------------- Clustering With Scaling ----------------- #
# Only scale numeric columns (not the encoded category)
scaler = StandardScaler()
X_scaled = X.copy()
X_scaled[['mileage', 'fuel_efficiency', 'maintenance_cost']] = scaler.fit_transform(
    X_scaled[['mileage', 'fuel_efficiency', 'maintenance_cost']]
)

kmeans_scaled = KMeans(n_clusters=3, random_state=0)
df['cluster_scaled'] = kmeans_scaled.fit_predict(X_scaled)

# ----------------- Show Results ----------------- #
print("\nCluster assignments without and with scaling:")
print(df[['vehicle_serial_no', 'vehicle_type', 'cluster_no_scaling', 'cluster_scaled']])

# ----------------- Optional Visualization ----------------- #
plt.figure(figsize=(12, 5))

# Without scaling
plt.subplot(1, 2, 1)
sns.scatterplot(data=df, x='mileage', y='maintenance_cost', hue='cluster_no_scaling', palette='Set1')
plt.title("K-Means Clustering Without Scaling")

# With scaling
plt.subplot(1, 2, 2)
sns.scatterplot(data=df, x='mileage', y='maintenance_cost', hue='cluster_scaled', palette='Set2')
plt.title("K-Means Clustering With Scaling")

plt.tight_layout()
plt.show()


# A transportation company wants to optimize its routes and fleet by categorizing
# different types of vehicles based on their usage patterns. The company has data on
# several features such as: vehicle_serial_no, mileage, fuel_efficiency, maintenance_cost,
# and vehicle_type. The goal is to create segments of vehicles based on these attributes to
# help with fleet management. Implement K-Means clustering to group vehicles using all
# the features. Perform the clustering twice: once without scaling the features and once
# with scaling applied to all features (except for vehicle_type, which is categorical).
# Analyze and compare the results, focusing on how the scaling affects the clustering
# output.
# Sample Data:
# # Example vehicle data
# data = {
#  ‘vehicle_serial_no’: [5, 3, 8, 2, 4, 7, 6, 10, 1, 9],
#  'mileage': [150000, 120000, 250000, 80000, 100000, 220000, 180000, 300000,
# 75000, 280000],
#  'fuel_efficiency': [15, 18, 10, 22, 20, 12, 16, 8, 24, 9],
#  'maintenance_cost': [5000, 4000, 7000, 2000, 3000, 6500, 5500, 8000, 1500, 7500],
#  'vehicle_type': ['SUV', 'Sedan', 'Truck', 'Hatchback', 'Sedan', 'Truck', 'SUV', 'Truck',
# 'Hatchback', 'SUV']
# }
# # Create a DataFrame
# df = pd.DataFrame(data)
