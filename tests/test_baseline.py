import pytest
import baseline.tasks

@pytest.mark.req("BASELINE-04")
def test_first_missing():
    required = ["item1", "item2", "item3"]
    present = ["item1", "item3"]
    assert baseline.tasks.first_missing(required, present) == "item2"

