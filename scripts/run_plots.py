"""Small CLI to generate plots and save them to `outputs/` by default."""
import argparse
from project_report import data
from project_report import plotting


def main(out_dir: str):
    plotting.coding_speed_average(data.times_by_stage, out_dir)
    plotting.plot_performance_vs_ideal(data.performance, data.perfect_list, out_dir)
    # subjective plot requires confidence and concentration arrays; reuse example arrays from original scripts
    confidence = [
        [None, 3, 2, 1],
        [None, 4, 4, 1],
        [None, 4, 4, 3],
        [None, 3, 2, 1],
        [None, 2, 2, 1],
        [None, 5, 4, 2],
        [None, 3, 2, 1],
        [None, 3, 2, 1],
        [None, 3, 2, 1],
        [None, 3, 3, 1]
    ]
    concentration = [
        [4, 3, 2, 1],
        [3, 3, 2, 1],
        [4, 4, 3, 2],
        [4, 4, 3, 1],
        [5, 3, 2, 1],
        [5, 5, 4, 3],
        [4, 3, 2, 1],
        [4, 4, 2, 1],
        [5, 3, 2, 1],
        [4, 4, 3, 2]
    ]
    plotting.plot_subjective_assessment(data.performance, confidence, concentration, data.perfect_list, out_dir)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate analysis plots')
    parser.add_argument('--out', '-o', default='outputs', help='Output directory')
    args = parser.parse_args()
    main(args.out)
