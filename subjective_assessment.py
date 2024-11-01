import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Data: Lines of Code (actual performance)
performance = [
    [10, 3, 28, 12],  # Nik
    [10, 7, 13, None],  # nickname
    [18, 5, 12, 10],  # animal012
    [7, 8, 16, 17],  # Vova
    [6, 7, 12, 18],  # Mark
    [11, 12, 19, 15],  # Z
    [9, 8, 7, 10],  # Bob
    [9, 3, 14, None],  # Carol
    [7, 5, 14, 7],   # Dave
    [8, 2, 2, None]    # Alice
]
df_performance = pd.DataFrame(performance, columns=['Sober', '1 Drink', '2 Drinks', '3 Drinks'])

# Ideal number of lines of code for each stage
perfect_list = [6, 2, 3, 6]
perfect_series = pd.Series(perfect_list, index=df_performance.columns)

# Calculate the gap from the ideal performance (difference from perfect)
performance_gap = df_performance.sub(perfect_series).abs()
average_performance_gap = performance_gap.mean()

# Data: Confidence Levels
confidence_levels = [
    [None, 3, 2, 1],  # Nik
    [None, 4, 4, 1],  # nickname
    [None, 4, 4, 3],  # animal012
    [None, 3, 2, 1],  # Vova
    [None, 2, 2, 1],  # Mark
    [None, 5, 4, 2],  # Z
    [None, 3, 2, 1],  # Bob
    [None, 3, 2, 1],  # Carol
    [None, 3, 2, 1],   # Dave
    [None, 3, 3, 1]    # Alice
]
df_confidence = pd.DataFrame(confidence_levels, columns=['Sober', '1 Drink', '2 Drinks', '3 Drinks'])
average_confidence = df_confidence.mean()

# Data: Concentration Levels
concentration_levels = [
    [4, 3, 2, 1],  # Nik
    [3, 3, 2, 1],  # nickname
    [4, 4, 3, 2],  # animal012
    [4, 4, 3, 1],  # Vova
    [5, 3, 2, 1],  # Mark
    [5, 5, 4, 3],  # Z
    [4, 3, 2, 1],  # Bob
    [4, 4, 2, 1],  # Carol
    [5, 3, 2, 1],   # Dave
    [4, 4, 3, 2]    # Alice
]
df_concentration = pd.DataFrame(concentration_levels, columns=['Sober', '1 Drink', '2 Drinks', '3 Drinks'])
average_concentration = df_concentration.mean()

# Plotting
fig, axs = plt.subplots(3, 1, figsize=(10, 18))
plt.subplots_adjust(hspace=0.5)

# Plot 1: Average Performance Gap (Difference from Ideal Performance)
sns.barplot(x=average_performance_gap.index, y=average_performance_gap.values, palette="coolwarm", ax=axs[0])
axs[0].set_title("Average Performance Gap by Stage (Difference from Ideal)")
axs[0].set_ylabel("Average Gap from Ideal (Lines of Code)")
axs[0].set_xlabel("Alcohol Consumption Stage")
axs[0].axhline(0, color="black", linewidth=0.5, linestyle="--")  # Reference line for ideal

# Plot 2: Average Confidence Levels (Subjective Perception)
sns.barplot(x=average_confidence.index, y=average_confidence.values, palette="coolwarm", ax=axs[1])
axs[1].set_title("Average Confidence Levels by Stage (Subjective)")
axs[1].set_ylabel("Average Confidence Level (1-5)")
axs[1].set_xlabel("Alcohol Consumption Stage")

# Plot 3: Average Concentration Levels (Subjective Perception)
sns.barplot(x=average_concentration.index, y=average_concentration.values, palette="coolwarm", ax=axs[2])
axs[2].set_title("Average Concentration Levels by Stage (Subjective)")
axs[2].set_ylabel("Average Concentration Level (1-5)")
axs[2].set_xlabel("Alcohol Consumption Stage")

plt.show()
