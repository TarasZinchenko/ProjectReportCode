from scipy.stats import pearsonr
import numpy as np

# Map experience levels to numerical values for correlation analysis
experience_mapping = {
    "Less than 1 year": 1,
    "1-3 years": 2,
    "3-5 years": 3
}
participant_data = {
    "Nik": {"age": 20, "height": 186, "weight": 84, "drinking_frequency": "Occasionally", "experience": "3-5 years"},
    "nickname": {"age": 18, "height": 192, "weight": 80, "drinking_frequency": "Occasionally", "experience": "1-3 years"},
    "animal012": {"age": 19, "height": 173, "weight": 66, "drinking_frequency": "Regularly", "experience": "3-5 years"},
    "Vova": {"age": 20, "height": 184, "weight": 76, "drinking_frequency": "Regularly", "experience": "Less than 1 year"},
    "Mark": {"age": 21, "height": 175, "weight": 65, "drinking_frequency": "Occasionally", "experience": "1-3 years"},
    "Z": {"age": 19, "height": 168, "weight": 56, "drinking_frequency": "Occasionally", "experience": "3-5 years"},
    "Bob": {"age": 25, "height": 180, "weight": 75, "drinking_frequency": "Regularly", "experience": "3-5 years"},
    "Carol": {"age": 24, "height": 165, "weight": 60, "drinking_frequency": "Occasionally", "experience": "Less than 1 year"},
    "Dave": {"age": 27, "height": 175, "weight": 70, "drinking_frequency": "Regularly", "experience": "3-5 years"},
    "Alice": {"age": 23, "height": 160, "weight": 55, "drinking_frequency": "Occasionally", "experience": "1-3 years"}
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

# Function to perform correlation analysis between experience level and average coding speed
def correlation_experience_times(times_by_stage, participant_data, stages):
    experience_values = [experience_mapping[participant_data[name]["experience"]] for name in participant_data]
    correlations = {}

    for stage_index, stage in enumerate(stages):
        # Collect times for each participant at the current stage, ignoring None values
        stage_times = [times[stage_index] if times[stage_index] is not None else np.nan for times in times_by_stage]

        # Filter out participants with NaN times for this stage
        valid_times = [time for time in stage_times if not np.isnan(time)]
        valid_experience = [experience_values[i] for i, time in enumerate(stage_times) if not np.isnan(time)]

        # Perform Pearson correlation if there are enough data points
        if len(valid_times) > 1:
            corr, p_value = pearsonr(valid_experience, valid_times)
            correlations[stage] = {"correlation": corr, "p_value": p_value}
        else:
            correlations[stage] = {"correlation": None, "p_value": None}  # Not enough data points

    return correlations


stages = ["Sober", "1 Drink", "2 Drinks", "3 Drinks"]
correlation_results = correlation_experience_times(times_by_stage, participant_data, stages)

for stage, result in correlation_results.items():
    if result["correlation"] is not None:
        print(f"Stage '{stage}': Correlation = {result['correlation']:.2f}, p-value = {result['p_value']:.3f}")
    else:
        print(f"Stage '{stage}': Not enough data for correlation analysis")
