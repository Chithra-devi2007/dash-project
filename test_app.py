import pytest
from dash.testing.application_runners import ThreadedRunner
from dash.testing.browser import Browser

# Namma app.py-la irundhu 'app' object-ai import செய்கிறோம்
from app import app


@pytest.fixture
def dash_duo(dash_threaded_runner, selenium):
    """Dash testing-காக browser மற்றும் runner-ஐ தயார் செய்யும் fixture."""
    return Browser(dash_threaded_runner, selenium)


# Test 1: Header இருக்கிறதா என்று சோதித்தல்
def test_header_present(dash_duo):
    dash_duo.start_server(app)

    # Header element இருக்கான்னு செக் பண்ணுது
    header = dash_duo.find_element("header")
    assert header is not None
    assert "Soul Foods Pink Morsel Sales Visualizer" in header.text


# Test 2: Visualisation Chart (Graph) இருக்கிறதா என்று சோதித்தல்
def test_visualization_present(dash_duo):
    dash_duo.start_server(app)

    # Graph component (id='sales-line-chart') இருக்கான்னு செக் பண்ணுது
    graph = dash_duo.find_element("#sales-line-chart")
    assert graph is not None


# Test 3: Region Picker (Radio Items) இருக்கிறதா என்று சோதித்தல்
def test_region_picker_present(dash_duo):
    dash_duo.start_server(app)

    # Radio items (id='region-filter') இருக்கான்னு செக் பண்ணுது
    radio_items = dash_duo.find_element("#region-filter")
    assert radio_items is not None
