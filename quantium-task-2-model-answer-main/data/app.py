import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

# Load the data
df = pd.read_csv('formatted_data.csv')

# Create a Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div(children=[
    html.H1(children='Pink Morsel Sales Data Visualizer'),
    
    html.Div(children='''
        Sales Data Visualization for Soul Foods.
    '''),
    
    dcc.Graph(
        id='sales-line-chart',
        figure={}
    )
])

# Create the figure
def create_figure(df):
    fig = px.line(df, x='date', y='sales', color='region', title='Pink Morsel Sales Over Time')
    fig.update_layout(
        xaxis_title='Date',
        yaxis_title='Sales'
    )
    return fig

# Update the figure when the app starts
@app.callback(
    dash.dependencies.Output('sales-line-chart', 'figure'),
    [dash.dependencies.Input('sales-line-chart', 'id')]
)
def update_figure(input_value):
    return create_figure(df)

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
