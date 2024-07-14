###THIS SCRIPT MIGHT TAKE 10-30 SECONDS TO RUN
import requests
from bs4 import BeautifulSoup
from app import app, db, Discovery, EconomicData
import re
import pandas as pd
# import time

# def timing_decorator(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         print(f"{func.__name__} executed in: {end_time - start_time:.4f} seconds")
#         return result
#     return wrapper


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

def extract_year(text):
    """Extracts the first year mentioned in the text that falls within the range of 1700 to 2024."""
    match = re.search(r'\b(17[0-9]{2}|18[0-9]{2}|19[0-9]{2}|20[01][0-9]|202[0-4])\b', text)
    return match.group(1) if match else 'Unknown'

#@timing_decorator
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
                page_id = result['pageid']

                # Fetch the full page content to extract the date
                page_response = requests.get(API_ENDPOINT, params={
                    'action': 'parse',
                    'pageid': page_id,
                    'prop': 'wikitext',
                    'format': 'json'
                })
                try:
                    page_data = page_response.json()
                    wikitext = page_data['parse']['wikitext']['*']
                    year = extract_year(wikitext)
                except (requests.exceptions.JSONDecodeError, KeyError):
                    year = 'Unknown'

                event_entry = Discovery(
                    name=result['title'],
                    date=year,
                    description=clean_snippet,
                    category='Scientific Discovery'  # Adjust as needed
                )
                db.session.add(event_entry)
        db.session.commit()
        print("Historical events data added successfully.")

#@timing_decorator
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
