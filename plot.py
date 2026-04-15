import matplotlib.pyplot as plt
import numpy as np

def plot_graph(X, y, model):
    # Convert to array
    X_vals = X.values.flatten()
    y_vals = y.values

    # Smooth line
    X_range = np.linspace(X_vals.min(), X_vals.max() + 5, 100).reshape(-1, 1)
    y_pred_line = model.predict(X_range)

    # Prediction point
    next_month = X_vals.max() + 1
    predicted_value = model.predict([[next_month]])

    # Plot
    plt.figure(figsize=(10, 6))

    # Actual data
    plt.scatter(X_vals, y_vals, color='blue', label='Actual Data', s=60)

    # Regression line
    plt.plot(X_range, y_pred_line, color='red', linewidth=2, label='Prediction Line')

    # Prediction point
    plt.scatter(next_month, predicted_value, color='green', s=100, label='Next Month Prediction')

    # Labels
    plt.xlabel("Month", fontsize=12)
    plt.ylabel("Expense", fontsize=12)
    plt.title("Monthly Expense Prediction (Enhanced)", fontsize=14)

    # Grid & legend
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()

    plt.show()