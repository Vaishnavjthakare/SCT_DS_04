"""
Task 04: Traffic Accident Data Analysis
Analyze patterns related to road conditions, weather, and time of day.
Visualize accident hotspots and contributing factors.
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# ---- Step 1: Create Sample Dataset ----

np.random.seed(42)
n = 200

data = {
    'Hour': np.random.choice(range(24), n),
    'Weather': np.random.choice(['Clear', 'Rain', 'Fog', 'Snow'], n),
    'Road_Condition': np.random.choice(['Dry', 'Wet', 'Icy'], n),
    'Severity': np.random.choice([1, 2, 3], n),
    'Factor': np.random.choice(['Speeding', 'Distracted', 'Drunk'], n),
}

df = pd.DataFrame(data)
df.to_csv('accident_data.csv', index=False)
print("Dataset saved: 200 records\n")

# ---- Step 2: Basic Analysis ----

print("Shape:", df.shape)
print("\nFirst 5 rows:")
print(df.head())

print("\nAccidents by Weather:")
print(df['Weather'].value_counts())

print("\nAccidents by Road Condition:")
print(df['Road_Condition'].value_counts())

print("\nTop Contributing Factors:")
print(df['Factor'].value_counts())

# ---- Step 3: Visualizations (3 charts) ----

os.makedirs('output', exist_ok=True)

# Chart 1: Weather conditions
plt.figure(figsize=(6, 4))
df['Weather'].value_counts().plot(kind='bar', color=['gold', 'skyblue', 'gray', 'lightcoral'])
plt.title('Accidents by Weather')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('output/1_weather.png')
plt.close()
print("\nSaved: output/1_weather.png")

# Chart 2: Road conditions
plt.figure(figsize=(6, 4))
df['Road_Condition'].value_counts().plot(kind='bar', color=['sandybrown', 'cornflowerblue', 'lightblue'])
plt.title('Accidents by Road Condition')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('output/2_road.png')
plt.close()
print("Saved: output/2_road.png")

# Chart 3: Contributing factors
plt.figure(figsize=(6, 4))
df['Factor'].value_counts().plot(kind='bar', color=['teal', 'coral', 'mediumpurple'])
plt.title('Contributing Factors')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('output/3_factors.png')
plt.close()
print("Saved: output/3_factors.png")

# ---- Step 4: Key Findings ----

print("\n--- KEY FINDINGS ---")
print("Most common weather:", df['Weather'].mode()[0])
print("Most common road condition:", df['Road_Condition'].mode()[0])
print("Top contributing factor:", df['Factor'].mode()[0])
print("\nDone. Charts saved in output/ folder.")
