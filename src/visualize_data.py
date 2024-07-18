import pandas as pd
import plotly.graph_objects as go
from app import db, Discovery, EconomicData

def visualize():
    # Fetch data from the database
    with app.app_context():
        discoveries_query = db.session.query(Discovery).statement
        economic_data_query = db.session.query(EconomicData).statement

        discoveries = pd.read_sql(discoveries_query, db.engine)
        economic_data = pd.read_sql(economic_data_query, db.engine)

        # Ensure date formats are consistent
        discoveries['date'] = pd.to_datetime(discoveries['date'], errors='coerce').dropna()
        economic_data['year'] = pd.to_datetime(economic_data['year'], format='%Y')

        # Calculate cumulative discoveries over the past 30 years
        discoveries['year'] = discoveries['date'].dt.year
        cumulative_discoveries = discoveries.groupby('year').size().rolling(window=30, min_periods=1).sum()

        # Align cumulative discoveries with GDP data
        gdp_per_year = economic_data.set_index('year')['gdp']
        cumulative_discoveries.index = pd.to_datetime(cumulative_discoveries.index, format='%Y')
        gdp_per_year.index = pd.to_datetime(gdp_per_year.index, format='%Y')

        cumulative_discoveries = cumulative_discoveries.reindex(gdp_per_year.index, method='ffill').fillna(0)

    # Plot combined graph with Plotly
    fig = go.Figure()

    # Add cumulative discoveries
    fig.add_trace(go.Scatter(x=cumulative_discoveries.index, y=cumulative_discoveries.values,
                             mode='lines', name='Cumulative Discoveries'))

    # Add GDP
    fig.add_trace(go.Scatter(x=gdp_per_year.index, y=gdp_per_year.values,
                             mode='lines', name='GDP', yaxis='y2'))

    # Create axis objects
    fig.update_layout(
        title="Cumulative Discoveries and GDP Growth Over Time",
        xaxis=dict(title='Year'),
        yaxis=dict(title='Cumulative Discoveries'),
        yaxis2=dict(title='GDP', overlaying='y', side='right')
    )

    # Add zoom feature
    fig.update_layout(hovermode="x unified")

    # Save plot
    fig.write_html("templates/combined_graph.html")

if __name__ == '__main__':
    visualize()
