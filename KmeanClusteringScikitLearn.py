import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans, k_means

data = pd.read_csv(r"D:\Internship\3.12. Example.csv")
km = KMeans(n_clusters = 2, random_state = 0, n_init = "auto")
label = km.fit_predict(data)

centre = km.cluster_centers_

label0 = data[label == 0]
label1 = data[label == 1]

color = np.random.randint(10, 100, len(label0))
colors = np.random.randint(10, 100, len(label1))
plt.scatter(label0.iloc[:,0], label0.iloc[:,1], c = color, cmap = "Pastel2")
plt.scatter(label1.iloc[:,0], label1.iloc[:,1], c = colors, cmap = "BuPu")
plt.show()
print(abs(km.score(data)))
