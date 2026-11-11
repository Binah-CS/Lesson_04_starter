import pytest
from baseline.tasks import first_missing


@pytest.mark.req("BASELINE-04")
def test_first_missing_returns_first_required_item_not_present():
    assert first_missing(["a", "b", "c"], ["a", "c"]) == "b"
    assert first_missing(["a", "b", "c"], []) == "a"
    assert first_missing(["a", "b"], ["b", "a", "x"]) is None