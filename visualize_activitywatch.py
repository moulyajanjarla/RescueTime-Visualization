import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("activitywatch_data.csv")

# Count time spent per application
app_usage = df["app"].value_counts().head(10)  # Top 10 apps

# Plot
plt.figure(figsize=(12, 6))
sns.barplot(x=app_usage.values, y=app_usage.index, palette="viridis")
plt.xlabel("Usage Count")
plt.ylabel("Application")
plt.title("Most Used Applications (ActivityWatch)")
plt.show()