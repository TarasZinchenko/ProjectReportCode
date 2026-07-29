"""CLI to run statistical tests and save results to JSON."""
import argparse
import json
from project_report import data
from project_report import analysis


def main(out_file: str):
    experience_values = [data.experience_mapping[p["experience"]] for p in data.participant_data.values()]
    corr = analysis.correlation_experience_times(data.times_by_stage, experience_values, data.stages)
    ttests = analysis.paired_t_tests(data.times_by_stage, data.stages)
    wilc = analysis.wilcoxon_tests(data.times_by_stage, data.stages)

    results = {"correlation": corr, "t_tests": ttests, "wilcoxon": wilc}
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2)
    print(f"Results written to {out_file}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run statistical analyses and save results')
    parser.add_argument('--out', '-o', default='outputs/stats.json', help='Output JSON file')
    args = parser.parse_args()
    main(args.out)
