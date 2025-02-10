import torch
import torch.nn as nn
import torch.optim as optim
import pandas as pd
import numpy as np

# Load data
df = pd.read_csv("activitywatch_data.csv")
df["timestamp"] = pd.to_datetime(df["timestamp"])
df["time_spent"] = df.groupby("app")["timestamp"].transform("count")  # Aggregate time spent

# Select one app to predict usage
app_name = df["app"].value_counts().index[0]
app_data = df[df["app"] == app_name]["time_spent"].values

# Prepare training data
X = np.array(app_data[:-1]).reshape(-1, 1)
y = np.array(app_data[1:]).reshape(-1, 1)

X_train = torch.tensor(X, dtype=torch.float32)
y_train = torch.tensor(y, dtype=torch.float32)

# Define LSTM Model
class LSTMModel(nn.Module):
    def __init__(self):
        super(LSTMModel, self).__init__()
        self.lstm = nn.LSTM(1, 10, batch_first=True)
        self.fc = nn.Linear(10, 1)

    def forward(self, x):
        x, _ = self.lstm(x.view(len(x), 1, -1))
        x = self.fc(x[:, -1, :])
        return x

model = LSTMModel()
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

# Train the model
for epoch in range(500):
    optimizer.zero_grad()
    output = model(X_train)
    loss = criterion(output, y_train)
    loss.backward()
    optimizer.step()
    if epoch % 50 == 0:
        print(f"Epoch {epoch}, Loss: {loss.item()}")

# Save model
torch.save(model.state_dict(), "activitywatch_model.pth")
print("Model trained and saved!")