"""Basic tests that don't require heavy dependencies."""
from project_report import data


def test_data_lengths():
    assert len(data.participant_data) == len(data.times_by_stage) == len(data.performance)
    assert len(data.stages) == 4
