"""Baseline homework tests: import only baseline.tasks."""
import pytest

from baseline import tasks


@pytest.mark.req("BASELINE-04")
def test_first_missing_returns_first_required_item_not_present():
    assert tasks.first_missing(["med_1", "med_2", "med_3"], ["med_1", "med_3"]) == "med_2"
