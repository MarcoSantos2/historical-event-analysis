# src/visualize_data.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def visualize():
    # Load the data
    cumulative_discoveries = pd.read_csv('cumulative_discoveries.csv', index_col=0, parse_dates=True)
    gdp_per_year = pd.read_csv('gdp_per_year.csv', index_col=0, parse_dates=True)

    # Visualization
    plt.figure(figsize=(12, 6))

    # Plot cumulative discoveries
    plt.subplot(2, 1, 1)
    plt.plot(cumulative_discoveries, label='Cumulative Discoveries (last 30 years)', color='blue')
    plt.title('Cumulative Discoveries Over Time')
    plt.xlabel('Year')
    plt.ylabel('Cumulative Discoveries')
    plt.legend()

    # Plot GDP
    plt.subplot(2, 1, 2)
    plt.plot(gdp_per_year, label='GDP', color='green')
    plt.title('GDP Over Time')
    plt.xlabel('Year')
    plt.ylabel('GDP')
    plt.legend()

    plt.tight_layout()
    plt.savefig('discoveries_and_gdp_over_time.png')
    plt.show()

    # Scatter plot for correlation
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=cumulative_discoveries.squeeze(), y=gdp_per_year.squeeze())
    plt.title('Correlation between Cumulative Discoveries and GDP')
    plt.xlabel('Cumulative Discoveries (last 30 years)')
    plt.ylabel('GDP')
    plt.savefig('correlation_scatter_plot.png')
    plt.show()

if __name__ == '__main__':
    visualize()
