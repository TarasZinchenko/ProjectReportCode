from setuptools import setup, find_packages

setup(
    name="project_report",
    version="0.1.0",
    description="Analysis and plotting utilities for the ProjectReportCode",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    entry_points={
        'console_scripts': [
            'project-report-plots=project_report.cli:run_plots',
            'project-report-stats=project_report.cli:run_stats'
        ]
    },
)
