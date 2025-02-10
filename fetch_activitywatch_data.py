import requests
import pandas as pd

API_URL = "http://localhost:5600/api/0/buckets"

# Fetch list of all available buckets
response = requests.get(API_URL)
buckets = response.json()

# Select 'aw-watcher-window' bucket (tracks active application usage)
bucket_id = [b for b in buckets if "aw-watcher-window" in b][0]
data_url = f"http://localhost:5600/api/0/buckets/{bucket_id}/events"

response = requests.get(data_url)
data = response.json()

# Convert to DataFrame
df = pd.DataFrame(data)
df["timestamp"] = pd.to_datetime(df["timestamp"])  # Convert timestamp

# Extract application namee
df["app"] = df["data"].apply(lambda x: x.get("app", "Unknown") if isinstance(x, dict) else "Unknown")


# Save data
df.to_csv("activitywatch_data.csv", index=False)
print("Data saved to activitywatch_data.csv")