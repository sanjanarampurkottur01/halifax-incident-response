# Import packages
from dash import Dash, html, dash_table, dcc
import pandas as pd
import plotly.express as px

# Incorporate data
df = pd.read_csv('../data/incident_response.csv')

top_locations = df['INCIDENT_LOCATION'].value_counts().nlargest(20).index

filtered_df = df[df['INCIDENT_LOCATION'].isin(top_locations)]
# Initialize the app
app = Dash(__name__)

# App layout
app.layout = html.Div(
    style={'backgroundColor': '#FFFFFF'},  # Add background color here
    children=[
        html.H1(children='Incident Response Halifax', style={'textAlign': 'center'}),  # Center-align the heading
        dash_table.DataTable(data=df.to_dict('records'), page_size=10),
        dcc.Graph(figure=px.histogram(filtered_df, x='INCIDENT_LOCATION', y='INCIDENT_NUMBER', histfunc='count'))
    ]
)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
