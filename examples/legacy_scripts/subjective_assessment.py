import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Data: Lines of Code (actual performance)
performance = [
    [10, 3, 28, 12],  # user1
    [10, 7, 13, None],  # nickname
    [18, 5, 12, 10],  # animal012
    [7, 8, 16, 17],  # user2
    [6, 7, 12, 18],  # user3
    [11, 12, 19, 15],  # Z
    [9, 8, 7, 10],  # user4
    [9, 3, 14, None],  # user5
    [7, 5, 14, 7],   # user6
    [8, 2, 2, None]    # Nickie
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
    [None, 3, 2, 1],  # user1
    [None, 4, 4, 1],  # nickname
    [None, 4, 4, 3],  # animal012
    [None, 3, 2, 1],  # user2
    [None, 2, 2, 1],  # user3
    [None, 5, 4, 2],  # Z
    [None, 3, 2, 1],  # user4
    [None, 3, 2, 1],  # user5
    [None, 3, 2, 1],   # user6
    [None, 3, 3, 1]    # Nickie
]
df_confidence = pd.DataFrame(confidence_levels, columns=['Sober', '1 Drink', '2 Drinks', '3 Drinks'])
average_confidence = df_confidence.mean()

# Data: Concentration Levels
concentration_levels = [
    [4, 3, 2, 1],  # user1
    [3, 3, 2, 1],  # nickname
    [4, 4, 3, 2],  # animal012
    [4, 4, 3, 1],  # user2
    [5, 3, 2, 1],  # user3
    [5, 5, 4, 3],  # Z
    [4, 3, 2, 1],  # user4
    [4, 4, 2, 1],  # user5
    [5, 3, 2, 1],   # user6
    [4, 4, 3, 2]    # Nickie
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
