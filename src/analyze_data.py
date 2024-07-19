# src/analyze_data.py

import pandas as pd
from app import app, db, Discovery, EconomicData

def analyze():
    with app.app_context():
        # Fetch data from the database
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

        # Debug: Print correlation calculation inputs
        print("\nCumulative Discoveries (last 30 years) per year:")
        print(cumulative_discoveries)

        print("\nGDP per year:")
        print(gdp_per_year)

        # Calculate correlation
        correlation = cumulative_discoveries.corr(gdp_per_year)
        print(f"\nCorrelation between cumulative discoveries (last 30 years) and GDP: {correlation:.2f}")

        # Save results to CSV for further inspection
        cumulative_discoveries.to_csv('cumulative_discoveries.csv', header=['cumulative_discoveries'])

if __name__ == '__main__':
    analyze()
