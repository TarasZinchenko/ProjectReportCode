import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Participant data: Performance across four stages
performance = [
    [10, 3, 28, 12],  # user1
    [10, 7, 13, None],  # nickname
    [18, 5, 12, 10],  # animal012
    [7, 8, 16, 17],  # user3
    [6, 7, 12, 18],  # user4
    [11, 12, 19, 15],  # Z
    [9, 8, 7, 10],  # user5
    [9, 3, 14, None],  # user6
    [7, 5, 14, 7],   # user7
    [8, 2, 2, None]    # Nickie
]

# Ideal minimum lines for each stage
perfect_list = [6, 2, 3, 6]

# Convert the performance list into a DataFrame
df = pd.DataFrame(performance, columns=['Sober', '1 Drink', '2 Drinks', '3 Drinks'])

# Calculate the average performance at each stage (ignoring None values)
average_performance = df.mean()

# Convert ideal values into a Series for comparison
perfect_series = pd.Series(perfect_list, index=df.columns)

# Plot average performance for each stage with ideal values for comparison
plt.figure(figsize=(10, 6))

# Plot the average performance as bars
sns.barplot(x=average_performance.index, y=average_performance.values, color="steelblue", label="Average Performance")

# Plot the ideal values as bars with a lower alpha for transparency
sns.barplot(x=perfect_series.index, y=perfect_series.values, color="salmon", alpha=0.6, label="Ideal Performance")

# Add titles and labels
plt.title("Average Coding Performance vs Ideal by Stage")
plt.ylabel("Lines of Code")
plt.xlabel("Alcohol Consumption Stage")
plt.legend()
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()

# Plot gap from ideal performance
plt.figure(figsize=(10, 6))
sns.barplot(x=df.columns, y=df.sub(perfect_series).mean(), palette="coolwarm")
plt.title("Average Performance Gap from Ideal by Stage")
plt.ylabel("Average Gap from Ideal")
plt.xlabel("Alcohol Consumption Stage")
plt.axhline(0, color="black", linewidth=0.5, linestyle="--")  # Reference line for ideal
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()

# Plot change in average performance from Sober to 3 Drinks as a line plot
plt.figure(figsize=(10, 6))
sns.lineplot(x=average_performance.index, y=average_performance.values, marker='o', color="b", label="Average Performance")
sns.lineplot(x=perfect_series.index, y=perfect_series.values, marker='x', color="r", label="Ideal Performance")
plt.fill_between(average_performance.index, average_performance.values, perfect_series.values, color='gray', alpha=0.3)
plt.title("Performance Trend and Ideal Comparison")
plt.ylabel("Lines of Code")
plt.xlabel("Alcohol Consumption Stage")
plt.legend()
plt.grid(True)
plt.show()

# Display calculated percent change in performance
percent_change = (df['3 Drinks'].mean() - df['Sober'].mean()) / df['Sober'].mean() * 100
print(f"Percent Change from Sober to 3 Drinks: {percent_change:.2f}%")
