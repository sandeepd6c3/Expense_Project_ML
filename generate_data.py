import pandas as pd
import numpy as np

months = 20  # dataset size

data = []

base = 20000

for i in range(1, months + 1):
    # Trend + random variation
  expense = base + i * 300 + np.random.randint(-1000, 1000)
    data.append([i, expense])

df = pd.DataFrame(data, columns=["Month", "Expense"])
df.to_csv("data.csv", index=False)

print("Large dataset generated!")