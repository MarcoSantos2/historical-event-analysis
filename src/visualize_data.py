# src/visualize_data.py

import os
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from app import db, Discovery, EconomicData
import plotly.express as px
import statsmodels.api as sm

def visualize():
    discoveries = pd.read_csv('cumulative_discoveries.csv', index_col=0, parse_dates=True)
    gdp_per_year = pd.read_excel('mpd2020.xlsx', sheet_name='Full data', index_col='year', parse_dates=True)

    # Merge datasets on the date/year
    combined = discoveries.merge(gdp_per_year, left_index=True, right_index=True, how='inner')

    # Determine the absolute path to the static directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    static_dir = os.path.join(script_dir, '..', 'static')

    # Ensure the static directory exists
    os.makedirs(static_dir, exist_ok=True)

    # Create a subplot with 3 rows and 1 column
    fig = make_subplots(
        rows=3, cols=1,
        subplot_titles=("Cumulative Discoveries Over Time", "GDP Over Time", "Cumulative Discoveries and GDP Over Time"),
        specs=[[{"secondary_y": False}], [{"secondary_y": False}], [{"secondary_y": True}]]
    )

    # Add trace for cumulative discoveries (first subplot)
    fig.add_trace(
        go.Scatter(x=combined.index, y=combined['cumulative_discoveries'], name="Cumulative Discoveries", mode='lines', line=dict(color='blue')),
        row=1, col=1
    )

    # Add trace for GDP (second subplot)
    fig.add_trace(
        go.Scatter(x=combined.index, y=combined['gdppc'], name="GDP", mode='lines', line=dict(color='green')),
        row=2, col=1
    )

    # Add traces for dual y-axis plot (third subplot)
    fig.add_trace(
        go.Scatter(x=combined.index, y=combined['cumulative_discoveries'], name="Cumulative Discoveries", mode='lines', line=dict(color='blue')),
        row=3, col=1, secondary_y=False
    )

    fig.add_trace(
        go.Scatter(x=combined.index, y=combined['gdppc'], name="GDP per Capita", mode='lines', line=dict(color='red')),
        row=3, col=1, secondary_y=True
    )

    # Update layout for titles and axis labels
    fig.update_layout(
        title_text="Cumulative Discoveries and GDP Analysis",
        height=900  # Adjust height for better spacing
    )

    fig.update_xaxes(title_text="Year", row=1, col=1)
    fig.update_xaxes(title_text="Year", row=2, col=1)
    fig.update_xaxes(title_text="Year", row=3, col=1)

    fig.update_yaxes(title_text="Cumulative Discoveries", row=1, col=1)
    fig.update_yaxes(title_text="GDP", row=2, col=1)
    fig.update_yaxes(title_text="Cumulative Discoveries", row=3, col=1, secondary_y=False)
    fig.update_yaxes(title_text="GDP per Capita", row=3, col=1, secondary_y=True)

    # Save the plot as an HTML file
    fig.write_html(os.path.join(static_dir, 'discoveries_and_gdp_over_time.html'))

    # Visualization 2: Scatter plot for correlation
    fig2 = px.scatter(combined, x='cumulative_discoveries', y='gdppc',
                      title='Correlation between Cumulative Discoveries and GDP')

    # Add regression line
    X = combined['cumulative_discoveries']
    Y = combined['gdppc']
    X = sm.add_constant(X)  # Adds a constant term to the predictor
    model = sm.OLS(Y, X).fit()
    predictions = model.predict(X)

    fig2.add_trace(go.Scatter(x=combined['cumulative_discoveries'], y=predictions,
                              mode='lines', name='Linear Regression', line=dict(color='blue')))

    fig2.write_html(os.path.join(static_dir, 'correlation_scatter_plot_with_regression.html'))

    print("Plots created and saved as HTML files.")

if __name__ == '__main__':
    visualize()






# # src/visualize_data.py

# import pandas as pd
# import matplotlib.pyplot as plt
# import statsmodels.api as sm
# from app import db, Discovery, EconomicData

# def visualize():
#     discoveries = pd.read_csv('cumulative_discoveries.csv', index_col=0, parse_dates=True)
#     gdp_per_year = pd.read_excel('mpd2020.xlsx', sheet_name='Full data', index_col='year', parse_dates=True)

#     # Merge datasets on the date/year
#     combined = discoveries.merge(gdp_per_year, left_index=True, right_index=True, how='inner')

#     # Visualization 1: Cumulative Discoveries and GDP Over Time
#     plt.figure(figsize=(12, 6))

#     # Plot cumulative discoveries
#     plt.subplot(2, 1, 1)
#     plt.plot(combined.index, combined['cumulative_discoveries'], label='Cumulative Discoveries (last 30 years)', color='blue')
#     plt.title('Cumulative Discoveries Over Time')
#     plt.xlabel('Year')
#     plt.ylabel('Cumulative Discoveries')
#     plt.legend()

#     # Plot GDP
#     plt.subplot(2, 1, 2)
#     plt.plot(combined.index, combined['gdppc'], label='GDP', color='green')
#     plt.title('GDP Over Time')
#     plt.xlabel('Year')
#     plt.ylabel('GDP')
#     plt.legend()

#     plt.tight_layout()
#     plt.savefig('discoveries_and_gdp_over_time.png')
#     plt.show()

#     # Visualization 2: Scatter plot for correlation
#     plt.figure(figsize=(10, 6))
#     plt.scatter(combined['cumulative_discoveries'], combined['gdppc'], label='Data Points')

#     # Add regression line
#     X = sm.add_constant(combined['cumulative_discoveries'])  # Adds a constant term to the predictor
#     model = sm.OLS(combined['gdppc'], X).fit()
#     predictions = model.predict(X)

#     plt.plot(combined['cumulative_discoveries'], predictions, color='red', label='Regression Line')
    
#     # Add titles and labels
#     plt.title('Correlation between Cumulative Discoveries and GDP')
#     plt.xlabel('Cumulative Discoveries (last 30 years)')
#     plt.ylabel('GDP')

#     # Add legend
#     plt.legend()

#     # Save the plot
#     plt.savefig('correlation_scatter_plot_with_regression.png')
#     plt.show()

# if __name__ == '__main__':
#     visualize()
