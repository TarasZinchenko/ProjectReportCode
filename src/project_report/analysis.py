"""Statistical analysis helpers."""
from typing import List, Dict, Any
import numpy as np
from scipy.stats import pearsonr, ttest_rel, wilcoxon


def correlation_experience_times(times_by_stage: List[List[Any]], experience_values: List[int], stages: List[str]) -> Dict[str, Dict[str, Any]]:
    correlations = {}
    times_arr = np.array(times_by_stage, dtype=np.float64)

    for i, stage in enumerate(stages):
        stage_times = times_arr[:, i]
        valid = ~np.isnan(stage_times)
        if np.sum(valid) > 1:
            corr, p_value = pearsonr(np.array(experience_values)[valid], stage_times[valid])
            correlations[stage] = {"correlation": float(corr), "p_value": float(p_value)}
        else:
            correlations[stage] = {"correlation": None, "p_value": None}
    return correlations


def paired_t_tests(times_by_stage: List[List[Any]], stages: List[str]) -> Dict[str, Dict[str, float]]:
    results = {}
    times_arr = np.array(times_by_stage, dtype=np.float64)
    for i in range(len(stages) - 1):
        a = times_arr[:, i]
        b = times_arr[:, i + 1]
        valid = ~np.isnan(a) & ~np.isnan(b)
        key = f"{stages[i]} vs {stages[i+1]}"
        if np.sum(valid) > 1:
            stat, p = ttest_rel(a[valid], b[valid])
            results[key] = {"t_statistic": float(stat), "p_value": float(p)}
        else:
            results[key] = {"t_statistic": None, "p_value": None}
    return results


def wilcoxon_tests(times_by_stage: List[List[Any]], stages: List[str]) -> Dict[str, Dict[str, Any]]:
    results = {}
    times_arr = np.array(times_by_stage, dtype=np.float64)
    sober = times_arr[:, 0]
    for i in range(1, len(stages)):
        other = times_arr[:, i]
        valid = ~np.isnan(sober) & ~np.isnan(other)
        key = f"Sober vs {stages[i]}"
        if np.sum(valid) > 0:
            try:
                stat, p = wilcoxon(sober[valid], other[valid])
                results[key] = {"statistic": float(stat), "p_value": float(p)}
            except Exception:
                results[key] = {"statistic": None, "p_value": None}
        else:
            results[key] = {"statistic": None, "p_value": None}
    return results
