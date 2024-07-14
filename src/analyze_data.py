# src/analyze_data.py
import pandas as pd
from app import db, Discovery, EconomicData

def analyze():
    # Fetch data from the database
    discoveries = pd.read_sql(db.session.query(Discovery).statement, db.session.bind)
    economic_data = pd.read_sql(db.session.query(EconomicData).statement, db.session.bind)

    # Ensure date formats are consistent
    discoveries['date'] = pd.to_datetime(discoveries['date'], errors='coerce').dropna()
    economic_data['year'] = pd.to_datetime(economic_data['year'], format='%Y')

    # Merge datasets on the date/year
    combined = discoveries.merge(economic_data, left_on='date', right_on='year', how='inner')

    # Example Analysis 1: Correlation between number of discoveries and GDP
    discoveries_per_year = discoveries['date'].dt.year.value_counts().sort_index()
    gdp_per_year = economic_data.set_index('year')['gdp']

    correlation = discoveries_per_year.corr(gdp_per_year)
    print(f"Correlation between number of discoveries and GDP: {correlation:.2f}")

    # Example Analysis 2: Discoveries during significant GDP growth periods
    gdp_growth = economic_data['gdp'].pct_change().fillna(0)
    significant_growth_periods = economic_data[gdp_growth > 0.05]  # e.g., > 5% growth
    discoveries_during_growth = discoveries[discoveries['date'].dt.year.isin(significant_growth_periods['year'].dt.year)]

    print("Discoveries during significant GDP growth periods:")
    print(discoveries_during_growth)

    # Save results to CSV for further inspection
    combined.to_csv('combined_data.csv', index=False)
    discoveries_during_growth.to_csv('discoveries_during_growth.csv', index=False)

if __name__ == '__main__':
    analyze()