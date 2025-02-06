from scipy.stats import ttest_rel
import numpy as np


# Map experience levels to numerical values for correlation analysis
experience_mapping = {
    "Less than 1 year": 1,
    "1-3 years": 2,
    "3-5 years": 3
}
participant_data = {
    "user1": {"age": 20, "height": 186, "weight": 84, "drinking_frequency": "Occasionally", "experience": "3-5 years"},
    "nickname": {"age": 18, "height": 192, "weight": 80, "drinking_frequency": "Occasionally", "experience": "1-3 years"},
    "animal012": {"age": 19, "height": 173, "weight": 66, "drinking_frequency": "Regularly", "experience": "3-5 years"},
    "user2": {"age": 20, "height": 184, "weight": 76, "drinking_frequency": "Regularly", "experience": "Less than 1 year"},
    "user3": {"age": 21, "height": 175, "weight": 65, "drinking_frequency": "Occasionally", "experience": "1-3 years"},
    "Z": {"age": 19, "height": 168, "weight": 56, "drinking_frequency": "Occasionally", "experience": "3-5 years"},
    "user4": {"age": 25, "height": 180, "weight": 75, "drinking_frequency": "Regularly", "experience": "3-5 years"},
    "user5": {"age": 24, "height": 165, "weight": 60, "drinking_frequency": "Occasionally", "experience": "Less than 1 year"},
    "user6": {"age": 27, "height": 175, "weight": 70, "drinking_frequency": "Regularly", "experience": "3-5 years"},
    "Nickie": {"age": 23, "height": 160, "weight": 55, "drinking_frequency": "Occasionally", "experience": "1-3 years"}
}

# Data: Time spent by each student on each task (sober, 1 drink, 2 drinks, etc.)
times_by_stage = [
    [5, 2, 20, 10],  # Nik
    [11, 7, 21, None],  # nickname
    [11, 5, 12, 10],  # animal012
    [10, 8, 24, 34],  # Vova
    [9, 9, 18, 30],  # Mark
    [6, 3, 7, 13],  # Z
    [10, 5, 13, 19],  # Bob
    [15, 12, 24, None],  # Carol
    [9, 6, 15, 22],   # Dave
    [8, 6, 16, None]    # Alice
]

perfomance = [
    [10, 3, 28, 12],  # Nik
    [10, 7, 13, None],  # nickname
    [18, 5, 12, 10],  # animal012
    [7, 8, 24, 34],  # Vova
    [6, 9, 18, 30],  # Mark
    [11, 3, 7, 13],  # Z
    [10, 5, 13, 19],  # Bob
    [15, 12, 24, None],  # Carol
    [9, 6, 15, 22],   # Dave
    [8, 6, 16, None]    # Alice
]

# Convert times data to numpy array for easier manipulation
times_by_stage_array = np.array(times_by_stage, dtype=np.float64)  # Convert to float for handling None (NaN)

# Define the stages
stages = ["Sober", "1 Drink", "2 Drinks", "3 Drinks"]
results = {}

# Perform paired t-tests between consecutive stages
for i in range(len(stages) - 1):
    stage_1 = times_by_stage_array[:, i]
    stage_2 = times_by_stage_array[:, i + 1]

    # Filter out pairs with NaN values
    valid_pairs = ~np.isnan(stage_1) & ~np.isnan(stage_2)
    if np.sum(valid_pairs) > 1:  # Ensure at least two valid pairs for testing
        stat, p_value = ttest_rel(stage_1[valid_pairs], stage_2[valid_pairs])
        results[f"{stages[i]} vs {stages[i + 1]}"] = {"t-statistic": stat, "p-value": p_value}
    else:
        results[f"{stages[i]} vs {stages[i + 1]}"] = "Not enough valid pairs"

print(results)
