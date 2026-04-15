import pandas as pd
from sklearn.metrics import mean_squared_error
from model import train_model
from plot import plot_graph

# Load data
data = pd.read_csv("data.csv")

X = data[['Month']]
y = data['Expense']

# Train model
model = train_model(X, y)

# Predict next month
next_month = pd.DataFrame([[51]], columns=['Month'])
prediction = model.predict(next_month)

print("Predicted Expense for Month 51:", prediction[0])

# Calculate error (NEW)
y_pred = model.predict(X)
mse = mean_squared_error(y, y_pred)

print("Model Error (MSE):", mse)

# Plot
plot_graph(X, y, model)