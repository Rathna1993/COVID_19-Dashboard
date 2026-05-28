import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("C:\\Users\\Ashokmep\\Desktop\\Covid.csv")

# Print dataset
print(df)

# Create figure
plt.figure(figsize=(10,5))

# Cases graph
plt.plot(
    df["Day"],
    df["Cases"],
    marker='o',
    color='red',
    linewidth=3,
    label='Cases'
)

# Recoveries graph
plt.plot(
    df["Day"],
    df["Recoveries"],
    marker='o',
    color='green',
    linewidth=3,
    label='Recoveries'
)

# Deaths graph
plt.plot(
    df["Day"],
    df["Deaths"],
    marker='o',
    color='black',
    linewidth=3,
    label='Deaths'
)

# Add data labels
for i, value in enumerate(df["Cases"]):
    plt.text(i, value, str(value), ha='center')

for i, value in enumerate(df["Recoveries"]):
    plt.text(i, value, str(value), ha='center')

for i, value in enumerate(df["Deaths"]):
    plt.text(i, value, str(value), ha='center')

# Title and labels
plt.title("COVID-19 Dashboard")

plt.xlabel("Days")
plt.ylabel("Count")

# Legend
plt.legend()

# Grid
plt.grid(True)

# Show graph
plt.show()
