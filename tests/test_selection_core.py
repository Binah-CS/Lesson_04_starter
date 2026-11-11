"""Example tests (happy path only). They import only selection_core: the lesson 4 test rule."""
import pytest

import selection_core


@pytest.mark.req("REQ-SEL-01")
def test_valid_selection_is_returned(sample_event):
    selection = selection_core.submit_selection(sample_event, "cli_100", ["med_1"], ["add_to_album"])
    assert selection["media_ids"] == ["med_1"]
    assert selection["service_codes"] == ["add_to_album"]


@pytest.mark.req("REQ-SEL-01")
def test_valid_selection_is_recorded_on_the_event(sample_event):
    selection_core.submit_selection(sample_event, "cli_100", ["med_1", "med_2"], ["add_to_album"])
    assert len(sample_event["selections"]) == 1


@pytest.mark.req("REQ-SEL-03")
def test_available_services_lists_enabled_services_only(sample_event):
    assert selection_core.available_services(sample_event) == ["add_to_album"]


@pytest.mark.req("REQ-SEL-05")
def test_submit_selection_duplicate_media(sample_event):
    with pytest.raises(selection_core.SelectionError) as exc_info:
        selection_core.submit_selection(sample_event, "cli_100", ["med_1", "med_1"], ["add_to_album"])
    
    assert str(exc_info.value) == "DUPLICATE_MEDIA"



@pytest.mark.req("REQ-SEL-02")     
def test_media_from_another_event_is_rejected(sample_event):     
    with pytest.raises(selection_core.SelectionError) as err:     
        selection_core.submit_selection(   
            sample_event, "cli_100", ["med_999"], ["add_to_album"])     
 
    assert err.value.code == "MEDIA_NOT_IN_EVENT"     


@pytest.mark.req("REQ-SEL-06")
def test_unauthorized_client_is_forbidden(sample_event):
    with pytest.raises(selection_core.SelectionError) as err:
        selection_core.submit_selection(
            sample_event, "wrong_client", ["med_1"], ["add_to_album"])

    assert err.value.code == "FORBIDDEN"


    @pytest.mark.req("REQ-SEL-04")
def test_failed_selection_leaves_event_unchanged(sample_event):
    initial_selections_count = len(sample_event.get("selections", []))
    with pytest.raises(selection_core.SelectionError):
        selection_core.submit_selection(
            sample_event, "cli_100", [], ["add_to_album"])

    assert len(sample_event.get("selections", [])) == initial_selections_count