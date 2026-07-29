"""Command-line entry points for the project_report package."""
import argparse
from . import data
from . import plotting
from . import analysis
import json


def run_plots(argv=None):
    parser = argparse.ArgumentParser(description='Generate and save plots')
    parser.add_argument('--out', '-o', default='outputs', help='Output directory')
    args = parser.parse_args(argv)
    plotting.coding_speed_average(data.times_by_stage, args.out)
    plotting.plot_performance_vs_ideal(data.performance, data.perfect_list, args.out)
    # Provide example confidence/concentration arrays as before
    confidence = [
        [None, 3, 2, 1], [None, 4, 4, 1], [None, 4, 4, 3], [None, 3, 2, 1],
        [None, 2, 2, 1], [None, 5, 4, 2], [None, 3, 2, 1], [None, 3, 2, 1],
        [None, 3, 2, 1], [None, 3, 3, 1]
    ]
    concentration = [
        [4, 3, 2, 1], [3, 3, 2, 1], [4, 4, 3, 2], [4, 4, 3, 1],
        [5, 3, 2, 1], [5, 5, 4, 3], [4, 3, 2, 1], [4, 4, 2, 1],
        [5, 3, 2, 1], [4, 4, 3, 2]
    ]
    plotting.plot_subjective_assessment(data.performance, confidence, concentration, data.perfect_list, args.out)


def run_stats(argv=None):
    parser = argparse.ArgumentParser(description='Run statistical analyses and save results')
    parser.add_argument('--out', '-o', default='outputs/stats.json', help='Output JSON file')
    args = parser.parse_args(argv)
    experience_values = [data.experience_mapping[p['experience']] for p in data.participant_data.values()]
    corr = analysis.correlation_experience_times(data.times_by_stage, experience_values, data.stages)
    ttests = analysis.paired_t_tests(data.times_by_stage, data.stages)
    wilc = analysis.wilcoxon_tests(data.times_by_stage, data.stages)
    results = {"correlation": corr, "t_tests": ttests, "wilcoxon": wilc}
    with open(args.out, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2)
    print(f"Results written to {args.out}")


if __name__ == '__main__':
    # simple dispatch CLI
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == 'plots':
        run_plots(sys.argv[2:])
    elif len(sys.argv) > 1 and sys.argv[1] == 'stats':
        run_stats(sys.argv[2:])
    else:
        print('Usage: python -m project_report.cli [plots|stats] [--out <path>]')
