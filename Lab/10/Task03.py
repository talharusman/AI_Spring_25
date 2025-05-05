import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# ------------------ Step 1: Sample Student Data ------------------ #
data = {
    'student_id': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'GPA': [2.8, 3.5, 2.2, 3.9, 3.1, 2.5, 3.8, 3.0, 2.7, 3.6],
    'study_hours': [10, 20, 5, 25, 15, 8, 22, 13, 9, 21],
    'attendance_rate': [70, 85, 60, 95, 80, 65, 90, 75, 68, 88]
}

df = pd.DataFrame(data)

# ------------------ Step 2: Feature Selection and Scaling ------------------ #
features = df[['GPA', 'study_hours', 'attendance_rate']]
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

# ------------------ Step 3: Elbow Method ------------------ #
inertia = []
K_range = range(2, 7)

for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=0)
    kmeans.fit(features_scaled)
    inertia.append(kmeans.inertia_)

# Plot the elbow
plt.figure(figsize=(8, 5))
plt.plot(K_range, inertia, 'bo-')
plt.xlabel('Number of clusters (K)')
plt.ylabel('Inertia (WCSS)')
plt.title('Elbow Method For Optimal K')
plt.grid(True)
plt.show()

# ------------------ Step 4: Apply KMeans with Optimal K ------------------ #
# From elbow method, assuming optimal K = 3 (you can choose based on plot)
optimal_k = 3
kmeans_final = KMeans(n_clusters=optimal_k, random_state=0)
df['cluster'] = kmeans_final.fit_predict(features_scaled)

# ------------------ Step 5: Visualization ------------------ #
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='study_hours', y='GPA', hue='cluster', palette='Set1', s=100)
plt.title("Student Clustering Based on GPA and Study Hours")
plt.xlabel("Study Hours (Weekly Avg)")
plt.ylabel("GPA")
plt.legend(title="Cluster")
plt.grid(True)
plt.show()

# ------------------ Step 6: Final Output ------------------ #
print("Final Dataset with Cluster Assignments:")
print(df[['student_id', 'GPA', 'study_hours', 'attendance_rate', 'cluster']])


# The academic affairs department at FAST NUCES Karachi is looking to identify distinct
# groups of students based on their academic engagement and performance. The
# department has access to anonymized student data containing the attributes student_id,
# GPA, study_hours (average weekly study hours), and attendance_rate (percentage of
# classes attended).
# The goal is to group students into meaningful clusters that can help tailor academic
# support programs, such as extra tutoring, mentoring sessions, or motivation workshops.
# You are required to perform unsupervised learning using K-Means clustering on
# the student dataset. Do following :
# ● Feature Selection and Scaling: Use the following features for clustering: GPA,
# study_hours, and attendance_rate.
# ● Apply appropriate feature scaling before clustering.
# ● Determine Optimal Number of Clusters (K): Use the ELbow method to determine
# the optimal number of clusters (K) in the range of 2 to 6.
# ● Perform Clustering: Apply K-Means using the optimal K and assign a cluster label
# to each student.
# ● Visualization: Create a scatter plot to visualize the clusters using study_hours and
# GPA as the axes.
# ● Color each point based on its cluster.
# ● Add an informative title and labels for clarity.
# ● Deliverables: Display the final dataset showing student IDs along with their
# assigned cluster.
# ● Present the scatter plot that illustrates the clustering result.