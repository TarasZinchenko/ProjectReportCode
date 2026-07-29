"""Plotting helpers that save figures to files instead of showing them interactively."""
from typing import List, Dict, Any, Optional
import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def ensure_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def save_figure(fig, out_path: str) -> str:
    fig.tight_layout()
    fig.savefig(out_path)
    plt.close(fig)
    return out_path


def coding_speed_average(times_by_stage: List[List[Any]], out_dir: str, filename: str = "coding_speed_average.png") -> str:
    ensure_dir(out_dir)
    stages = ["Sober", "1 Drink", "2 Drinks", "3 Drinks"]
    times_arr = np.array(times_by_stage, dtype=np.float64)
    average_times = np.nanmean(times_arr, axis=0)

    fig, ax = plt.subplots(figsize=(10, 6))
    for i in range(times_arr.shape[0]):
        ax.plot(stages, [x if not np.isnan(x) else np.nan for x in times_arr[i, :]], marker='o', linestyle='-', label=f"Participant {i+1}")
    ax.plot(stages, average_times, marker='o', linestyle='--', color='black', linewidth=2, label='Average')
    ax.set_xlabel('Alcohol Consumption Level')
    ax.set_ylabel('Time Spent on Task (minutes)')
    ax.set_title('Coding Speed by Alcohol Consumption Level')
    ax.legend()
    ax.grid(True)
    return save_figure(fig, os.path.join(out_dir, filename))


def plot_performance_vs_ideal(performance: List[List[Any]], perfect_list: List[float], out_dir: str, filename: str = 'performance_vs_ideal.png') -> str:
    ensure_dir(out_dir)
    import pandas as pd
    df = pd.DataFrame(performance, columns=['Sober', '1 Drink', '2 Drinks', '3 Drinks'])
    perfect_series = pd.Series(perfect_list, index=df.columns)

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=df.columns, y=df.mean(), color='steelblue', label='Average Performance', ax=ax)
    sns.barplot(x=perfect_series.index, y=perfect_series.values, color='salmon', alpha=0.6, label='Ideal Performance', ax=ax)
    ax.set_title('Average Coding Performance vs Ideal by Stage')
    ax.set_ylabel('Lines of Code')
    ax.set_xlabel('Alcohol Consumption Stage')
    ax.legend()
    return save_figure(fig, os.path.join(out_dir, filename))


def plot_subjective_assessment(performance: List[List[Any]], confidence: List[List[Any]], concentration: List[List[Any]], perfect_list: List[float], out_dir: str, filename: str = 'subjective_assessment.png') -> str:
    ensure_dir(out_dir)
    import pandas as pd
    df_performance = pd.DataFrame(performance, columns=['Sober', '1 Drink', '2 Drinks', '3 Drinks'])
    df_confidence = pd.DataFrame(confidence, columns=['Sober', '1 Drink', '2 Drinks', '3 Drinks'])
    df_concentration = pd.DataFrame(concentration, columns=['Sober', '1 Drink', '2 Drinks', '3 Drinks'])
    perfect_series = pd.Series(perfect_list, index=df_performance.columns)

    avg_gap = df_performance.sub(perfect_series).abs().mean()
    avg_conf = df_confidence.mean()
    avg_conc = df_concentration.mean()

    fig, axs = plt.subplots(3, 1, figsize=(10, 18))
    sns.barplot(x=avg_gap.index, y=avg_gap.values, palette='coolwarm', ax=axs[0])
    axs[0].set_title('Average Performance Gap by Stage (Difference from Ideal)')
    axs[0].axhline(0, color='black', linewidth=0.5, linestyle='--')

    sns.barplot(x=avg_conf.index, y=avg_conf.values, palette='coolwarm', ax=axs[1])
    axs[1].set_title('Average Confidence Levels by Stage (Subjective)')

    sns.barplot(x=avg_conc.index, y=avg_conc.values, palette='coolwarm', ax=axs[2])
    axs[2].set_title('Average Concentration Levels by Stage (Subjective)')

    return save_figure(fig, os.path.join(out_dir, filename))
