# src/analyze_data.py
import pandas as pd
from app import db, Discovery, EconomicData

def analyze():
    discoveries = pd.read_sql(db.session.query(Discovery).statement, db.session.bind)
    economic_data = pd.read_sql(db.session.query(EconomicData).statement, db.session.bind)

    # Example analysis: finding discoveries around major GDP growth periods
    combined = discoveries.merge(economic_data, left_on='date', right_on='year', how='inner')
    print(combined)

if __name__ == '__main__':
    analyze()
