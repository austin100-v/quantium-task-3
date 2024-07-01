import pytest
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import dash.testing.application_runners as app_runner

# Import the app
from app import app

@pytest.fixture
def dash_duo():
    return app_runner.DashComposite()

def test_header_present(dash_duo):
    dash_duo.start_server(app)
    header = dash_duo.find_element('h1')
    assert header.text == "Pink Morsels Sales Data"

def test_visualisation_present(dash_duo):
    dash_duo.start_server(app)
    graph = dash_duo.find_element('#sales-graph')
    assert graph is not None

def test_region_picker_present(dash_duo):
    dash_duo.start_server(app)
    radio_items = dash_duo.find_element('#region-filter')
    assert radio_items is not None

if __name__ == '__main__':
    pytest.main()
