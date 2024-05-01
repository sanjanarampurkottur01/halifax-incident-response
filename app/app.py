# Import packages
from dash import Dash, html, dash_table, dcc
import pandas as pd
import plotly.express as px

# Incorporate data
df = pd.read_csv('./data/processed_incident.csv')

top_locations = df['CITY'].value_counts().nlargest(20).index

# Filter the DataFrame to include only the rows where 'INCIDENT_LOCATION' is in the top 20
filtered_df = df[df['CITY'].isin(top_locations)]

# Initialize the app
app = Dash(__name__)

# App layout
app.layout = html.Div([
    html.H1(style={'textAlign': "center"}, children='Halifax Incidents'),
    dash_table.DataTable(data=df.to_dict('records'), page_size=10),
    dcc.Graph(figure=px.histogram(filtered_df, x='CITY', y='INCIDENT_NUMBER', histfunc='count'))
])

# Define the server variable explicitly
server = app.server

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
