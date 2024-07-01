import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# Load the data
df = pd.read_csv('formatted_sales_data.csv')

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the app layout
app.layout = html.Div([
    html.H1("Pink Morsels Sales Data"),
    dcc.RadioItems(
        id='region-filter',
        options=[
            {'label': 'North', 'value': 'north'},
            {'label': 'East', 'value': 'east'},
            {'label': 'South', 'value': 'south'},
            {'label': 'West', 'value': 'west'},
            {'label': 'All', 'value': 'all'}
        ],
        value='all',
        inline=True
    ),
    dcc.Graph(id='sales-graph'),
    html.Link(href='style.css', rel='stylesheet')
])

# Define callback to update graph
@app.callback(
    Output('sales-graph', 'figure'),
    [Input('region-filter', 'value')]
)
def update_graph(selected_region):
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'] == selected_region]

    fig = px.line(filtered_df, x='date', y='sales', title='Sales Over Time', labels={'sales': 'Sales', 'date': 'Date'})
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
