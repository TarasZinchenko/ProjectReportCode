import matplotlib.pyplot as plt
import numpy as np

# Dictionary mapping participants' names to survey data
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
    [5, 2, 20, 10],  
    [11, 7, 21, None],  
    [11, 5, 12, 10],  
    [10, 8, 24, 34], 
    [9, 9, 18, 30],
    [6, 3, 7, 13],
    [10, 5, 13, 19],  
    [15, 12, 24, None], 
    [9, 6, 15, 22],
    [8, 6, 16, None]   
]

import matplotlib.pyplot as plt
import numpy as np


# Function for calculating and plotting average coding speed, handling None values
def coding_speed_average(times_by_stage):
    stages = ["Sober", "1 Drink", "2 Drinks", "3 Drinks"]
    num_stages = len(stages)

    # Calculate average while ignoring None values
    average_times = [
        np.nanmean([times[stage] if times[stage] is not None else np.nan for times in times_by_stage])
        for stage in range(num_stages)
    ]

    plt.figure(figsize=(10, 6))
    for i, times in enumerate(times_by_stage):
        times = [time if time is not None else np.nan for time in times]
        plt.plot(stages, times, marker='o', linestyle='-', label=f"Student {i + 1}")

    plt.plot(stages, average_times, marker='o', linestyle='--', color='black', linewidth=2, label="Average")
    plt.xlabel("Alcohol Consumption Level")
    plt.ylabel("Time Spent on Task (minutes)")
    plt.title("Coding Speed by Alcohol Consumption Level")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()



# Group participants by experience and weight
def group_by_experience_weight(participant_data):
    experience_groups = {
        "Less than 1 year": [], "1-3 years": [], "3-5 years": []
    }
    weight_groups = {"<70 kg": [], "70-80 kg": [], "80+ kg": []}

    for i, (name, data) in enumerate(participant_data.items()):
        experience = data["experience"]
        weight = data["weight"]
        if experience in experience_groups:
            experience_groups[experience].append(i)
        if weight < 70:
            weight_groups["<70 kg"].append(i)
        elif weight <= 80:
            weight_groups["70-80 kg"].append(i)
        else:
            weight_groups["80+ kg"].append(i)
    return experience_groups, weight_groups


# Plot trends by experience group, handling None values
def plot_by_experience(times_by_stage, experience_groups):
    stages = ["Sober", "1 Drink", "2 Drinks", "3 Drinks"]
    plt.figure(figsize=(10, 6))
    for exp, indices in experience_groups.items():
        avg_times = [
            np.nanmean([times_by_stage[i][stage] if times_by_stage[i][stage] is not None else np.nan for i in indices])
            for stage in range(len(stages))
        ]
        plt.plot(stages, avg_times, marker='o', linestyle='-', label=f"Experience: {exp}")
    plt.xlabel("Alcohol Consumption Level")
    plt.ylabel("Time Spent on Task (minutes)")
    plt.title("Coding Speed by Alcohol Consumption Level (Experience Groups)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


# Plot trends by drinking frequency, handling None values
def plot_by_drinking_frequency(times_by_stage, participant_data):
    # Map each frequency to participants by index
    frequency_groups = {"Occasionally": [], "Regularly": []}
    for i, (name, data) in enumerate(participant_data.items()):
        frequency = data["drinking_frequency"]
        if frequency in frequency_groups:
            frequency_groups[frequency].append(i)

    stages = ["Sober", "1 Drink", "2 Drinks", "3 Drinks"]
    plt.figure(figsize=(10, 6))
    for frequency, indices in frequency_groups.items():
        avg_times = [
            np.nanmean([times_by_stage[i][stage] if times_by_stage[i][stage] is not None else np.nan for i in indices])
            for stage in range(len(stages))
        ]
        plt.plot(stages, avg_times, marker='o', linestyle='-', label=f"Frequency: {frequency}")

    plt.xlabel("Alcohol Consumption Level")
    plt.ylabel("Time Spent on Task (minutes)")
    plt.title("Coding Speed by Alcohol Consumption Level (Drinking Frequency)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


# Plot trends by weight group, handling None values
def plot_by_weight(times_by_stage, weight_groups):
    stages = ["Sober", "1 Drink", "2 Drinks", "3 Drinks"]
    plt.figure(figsize=(10, 6))
    for weight, indices in weight_groups.items():
        avg_times = [
            np.nanmean([times_by_stage[i][stage] if times_by_stage[i][stage] is not None else np.nan for i in indices])
            for stage in range(len(stages))
        ]
        plt.plot(stages, avg_times, marker='o', linestyle='-', label=f"Weight: {weight}")
    plt.xlabel("Alcohol Consumption Level")
    plt.ylabel("Time Spent on Task (minutes)")
    plt.title("Coding Speed by Alcohol Consumption Level (Weight Groups)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


# Execute all plots with adjusted data handling
experience_groups, weight_groups = group_by_experience_weight(participant_data)
coding_speed_average(times_by_stage)
plot_by_experience(times_by_stage, experience_groups)
plot_by_weight(times_by_stage, weight_groups)
plot_by_drinking_frequency(times_by_stage, participant_data)


