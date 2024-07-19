# src/fetch_data.py

import requests
from bs4 import BeautifulSoup
from app import app, db, Discovery, EconomicData
import pandas as pd

API_ENDPOINT = 'https://en.wikipedia.org/w/api.php'
HISTORICAL_EVENTS = [
    'Steam Engine', 'Spinning Jenny', 'Electricity and Lightning Rod', 'Vaccination', 
    'Electric Telegraph', 'Telephone', 'Light Bulb', 'Photography', 'Pasteurization', 
    'Periodic Table', 'Airplane', 'Theory of Relativity', 'Quantum Mechanics', 
    'Penicillin', 'Radar', 'Nuclear Fission', 'DNA Structure', 'Computer', 'Internet', 
    'Laser', 'Moon Landing', 'Human Genome Project', 'Smartphones', 'CRISPR Gene Editing', 
    'Artificial Intelligence and Machine Learning', 'COVID-19 mRNA Vaccines'
]
MADDISON_FILE_PATH = '/mnt/d/repo/historical-event-analysis/src/mpd2020.xlsx'

def clean_html(raw_html):
    """Clean HTML content using BeautifulSoup."""
    soup = BeautifulSoup(raw_html, "html.parser")
    return soup.get_text()

def fetch_and_store_events():
    """Fetch historical events from Wikipedia and store in the database."""
    with app.app_context():
        for event in HISTORICAL_EVENTS:
            params = {
                'action': 'query',
                'list': 'search',
                'srsearch': event,
                'format': 'json',
                'redirects': 1,  # Follow redirects
                'srlimit': 1  # Limit to one result
            }
            response = requests.get(API_ENDPOINT, params=params)
            try:
                data = response.json()
            except requests.exceptions.JSONDecodeError:
                print(f"Failed to decode JSON for {event}: {response.text}")
                continue

            search_results = data.get('query', {}).get('search', [])
            if search_results:
                result = search_results[0]
                clean_snippet = clean_html(result['snippet'])

                # Leave the date column blank for manual entry later
                year = 'Unknown'

                event_entry = Discovery(
                    name=result['title'],
                    date=year,
                    description=clean_snippet,
                    category='Scientific Discovery'  # Adjust as needed
                )
                db.session.add(event_entry)
        db.session.commit()
        print("Historical events data added successfully. Please update the year column manually.")

def fetch_maddison_data():
    """Fetch economic data from the Maddison Project and store in the database."""
    df = pd.read_excel(MADDISON_FILE_PATH, sheet_name='Full data')
    with app.app_context():
        for index, row in df.iterrows():
            year = row['year']
            gdp = row['gdppc']
            if pd.notnull(gdp):  # Handle missing values
                existing_record = EconomicData.query.filter_by(year=year).first()
                if existing_record:
                    existing_record.gdp = gdp  # Update the existing record
                else:
                    new_record = EconomicData(year=year, gdp=gdp)  # Add a new record
                    db.session.add(new_record)
        db.session.commit()
        print("Maddison Project data added/updated successfully.")

def fetch_all_data():
    fetch_and_store_events()
    fetch_maddison_data()

if __name__ == '__main__':
    fetch_all_data()
