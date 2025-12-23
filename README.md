# K-Means Clustering: From-Scratch Initialization vs Scikit-Learn

This repository demonstrates **unsupervised learning using K-Means clustering**, implemented in two ways:

1. **Custom K-Means initialization logic (from scratch)** using Python, NumPy, and Pandas  
2. **Standard K-Means implementation using Scikit-learn**

The goal is to understand **how centroid initialization affects clustering behavior**, and to visually compare manual centroid selection with library-based optimization.

---

## 🔍 Project Overview

Clustering is a fundamental task in machine learning, especially in exploratory data analysis and biomedical signal/image processing.  
This project focuses on:

- Manual centroid initialization using **minimum and maximum y-values**
- Visualization of data points and initial centroids
- Comparison with Scikit-learn's optimized K-Means
- Understanding clustering loss (inertia)

---

## 📂 Dataset

- Input CSV file contains two numerical columns:
  - `x`: Feature 1  
  - `y`: Feature 2  

> ⚠️ **Note:**  
> Update the dataset path in the code before execution:
  pd.read_csv("path/to/your/Example.csv")

## ⚙️ Methodology
🔹 Part 1: Custom K-Means Initialization (From Scratch)

Reads the dataset using Pandas

Selects initial centroids as:

One point with minimum y-value

One point with maximum y-value

Removes these centroids from the dataset

## Visualizes:

Remaining data points

Initial cluster centroids

## 📊 This helps in understanding how centroid choice influences clustering outcomes.

🔹 Part 2: K-Means Using Scikit-learn

Uses KMeans from sklearn.cluster

Number of clusters: k = 2

Automatically optimized centroid initialization

Separates data based on predicted labels

Visualizes clusters using different color maps

Computes inertia (clustering error)

## 📈 Visualizations

The project includes:

Scatter plots of raw data

Highlighted initial centroids

Colored clusters from Scikit-learn

Comparison between manual and automated clustering

## 🧠 Key Learning Outcomes

Understanding centroid initialization strategies

Difference between manual vs optimized clustering

Visualization-driven interpretation of unsupervised learning

Practical use of Pandas, NumPy, Matplotlib, Seaborn, and Scikit-learn

## 🛠️ Technologies Used

Python 3.x

Pandas

NumPy

Matplotlib

Seaborn

Scikit-learn

## 🎯 Applications

Exploratory Data Analysis (EDA)

Biomedical signal/image clustering

Feature pattern discovery

Preprocessing for machine learning pipelines

## 📌 Future Improvements

Full iterative K-Means from scratch

Distance-based cluster assignment

Comparison with K-Means++

Extension to higher-dimensional datasets

Application to biomedical or sensor data

## 👤 Author

Soban Saeed
Machine Learning | Electrical & Biomedical Engineering Aspirant
GitHub: https://github.com/shizu75

## 📜 License

This project is open-source and available under the MIT License.
