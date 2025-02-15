from scipy.stats import wilcoxon

times_by_stage = [
    [5, 2, 20, 10],  # user1
    [11, 7, 21, None],  # nickname
    [11, 5, 12, 10],  # animal012
    [10, 8, 24, 34],  # user2
    [9, 9, 18, 30],  # user3
    [6, 3, 7, 13],  # Z
    [10, 5, 13, 19],  # user4
    [15, 12, 24, None],  # user5
    [9, 6, 15, 22],   # user6
    [8, 6, 16, None]    # Nickie
]

# Function to perform Wilcoxon Signed-Rank Tests on coding speed across alcohol consumption levels
def wilcoxon_test(times_by_stage):
    stages = ["Sober", "1 Drink", "2 Drinks", "3 Drinks"]
    results = {}

    for i in range(1, len(stages)):  # Compare "Sober" (index 0) with each subsequent stage
        sober_times = [times[0] for times in times_by_stage]  # Sober stage times
        stage_times = [times[i] for times in times_by_stage]  # Times for the current stage (1 drink, 2 drinks, etc.)

        # Perform Wilcoxon Signed-Rank Test between sober and current stage
        stat, p_value = wilcoxon(sober_times, stage_times)
        results[f"Sober vs {stages[i]}"] = {"statistic": stat, "p_value": p_value}

    return results


# Running the test function
wilcoxon_test(times_by_stage)
