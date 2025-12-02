import pandas as pd
import numpy as np

# Simulate 1000 data points of file modification behavior
# 500 samples for normal, 500 samples for ransomware

# Features: [time_to_modify (sec), num_files_modified, cpu_usage, disk_usage]
# Labels: 0 = Normal, 1 = Ransomware

np.random.seed(42)

# Normal activity (slow modifications)
normal_data = np.random.normal(loc=[10, 1, 50, 30], scale=[2, 1, 10, 5], size=(500, 4))
normal_labels = np.zeros(500)

# Ransomware activity (rapid modifications)
ransomware_data = np.random.normal(loc=[2, 15, 90, 80], scale=[1, 5, 10, 10], size=(500, 4))
ransomware_labels = np.ones(500)

# Combine the data
data = np.vstack([normal_data, ransomware_data])
labels = np.hstack([normal_labels, ransomware_labels])

# Create a DataFrame
df = pd.DataFrame(data, columns=["time_to_modify", "num_files_modified", "cpu_usage", "disk_usage"])
df["label"] = labels

# Save it to a CSV for later use
df.to_csv("ransomware_data.csv", index=False)

print("Dataset created and saved as ransomware_data.csv!")
