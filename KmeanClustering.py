import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
data = pd.read_csv(r"D:\Internship\3.12. Example.csv")
data = np.array(data)
data = pd.DataFrame(data, columns=['x', 'y'])

# Initialize clusters using min and max y
def cluster(data):
    cluster1 = data.min()
    cluster2 = data.max()
    m1 = data.y[data.y == cluster1.y].index.tolist()
    m2 = data.y[data.y == cluster2.y].index.tolist()
    cluster1 = data.iloc[m1[0]].values
    cluster2 = data.iloc[m2[0]].values
    data.drop(index=[m1[0], m2[0]], inplace=True)
    return cluster1, cluster2

# Assign data points to clusters (currently returns only centroids)
def weights(data):
    c1, c2 = cluster(data.copy())
    cluster1 = [c1]
    cluster2 = [c2]
    return cluster1, cluster2

# Call function and get initial clusters
cluster1, cluster2 = weights(data)
print("Cluster 1 centroid:", cluster1)
print("Cluster 2 centroid:", cluster2)

# Get clusters and remaining data for plotting
temp_data = data.copy()
c1, c2 = cluster(temp_data)
remaining_data = temp_data

# Plotting
plt.figure(figsize=(8, 6))
sns.scatterplot(data=remaining_data, x='x', y='y', color='gray', label='Remaining Points')
plt.scatter(c1[0], c1[1], color='blue', label='Cluster 1 (Min y)', s=100, marker='X')
plt.scatter(c2[0], c2[1], color='red', label='Cluster 2 (Max y)', s=100, marker='X')
plt.title('Initial Cluster Centroids and Data Points')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
