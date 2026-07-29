"""Shared dataset for analyses."""
from typing import List, Dict, Any

# Participant survey data
participant_data: Dict[str, Dict[str, Any]] = {
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

# Primary time/performance matrices (per participant order in participant_data)
times_by_stage: List[List[float]] = [
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

performance: List[List[float]] = [
    [10, 3, 28, 12],
    [10, 7, 13, None],
    [18, 5, 12, 10],
    [7, 8, 16, 17],
    [6, 7, 12, 18],
    [11, 12, 19, 15],
    [9, 8, 7, 10],
    [9, 3, 14, None],
    [7, 5, 14, 7],
    [8, 2, 2, None]
]

perfect_list: List[float] = [6, 2, 3, 6]

experience_mapping = {
    "Less than 1 year": 1,
    "1-3 years": 2,
    "3-5 years": 3
}

stages = ["Sober", "1 Drink", "2 Drinks", "3 Drinks"]
