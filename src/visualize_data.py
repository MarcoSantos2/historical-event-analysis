# visualize_data.py

import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from app import db, Discovery, EconomicData

def visualize():
    discoveries = pd.read_csv('cumulative_discoveries.csv', index_col=0, parse_dates=True)
    gdp_per_year = pd.read_excel('mpd2020.xlsx', sheet_name='Full data', index_col='year', parse_dates=True)

    # Merge datasets on the date/year
    combined = discoveries.merge(gdp_per_year, left_index=True, right_index=True, how='inner')

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(combined['cumulative_discoveries'], combined['gdppc'], label='Data Points')

    # Add regression line
    X = sm.add_constant(combined['cumulative_discoveries'])  # Adds a constant term to the predictor
    model = sm.OLS(combined['gdppc'], X).fit()
    predictions = model.predict(X)

    plt.plot(combined['cumulative_discoveries'], predictions, color='red', label='Regression Line')
    
    # Add titles and labels
    plt.title('Correlation between Cumulative Discoveries and GDP')
    plt.xlabel('Cumulative Discoveries (last 30 years)')
    plt.ylabel('GDP')

    # Add legend
    plt.legend()

    # Save the plot
    plt.savefig('correlation_scatter_plot_with_regression.png')
    plt.show()

if __name__ == '__main__':
    visualize()
