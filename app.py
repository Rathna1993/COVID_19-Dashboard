import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("C:\\Users\\Ashokmep\\Desktop\\Covid.csv")

print(df)

# Cases line graph
plt.plot(
    df["Day"],
    df["Cases"],
    marker='o',
    color='red',
    label='Cases'
)

# Recovery line graph
plt.plot(
    df["Day"],
    df["Recoveries"],
    marker='o',
    color='green',
    label='Recoveries'
)

# Labels
plt.title("COVID-19 Dashboard")

plt.xlabel("Day")
plt.ylabel("Count")

plt.legend()

plt.grid(True)

plt.show()