# src/fetch_data.py
import requests
from bs4 import BeautifulSoup
from app import app, db, Event

API_ENDPOINT = 'https://en.wikipedia.org/w/api.php'
HISTORICAL_EVENTS = ['World War II', 'Moon Landing', 'Fall of the Berlin Wall', 'American Revolution']

def clean_html(raw_html):
    soup = BeautifulSoup(raw_html, "html.parser")
    return soup.get_text()

def fetch_and_store_events():
    with app.app_context():
        for event in HISTORICAL_EVENTS:
            params = {
                'action': 'query',
                'list': 'search',
                'srsearch': event,
                'format': 'json'
            }
            response = requests.get(API_ENDPOINT, params=params)
            if response.status_code == 200:
                data = response.json()
                search_results = data.get('query', {}).get('search', [])
                for result in search_results:
                    clean_snippet = clean_html(result['snippet'])
                    event_entry = Event(
                        title=result['title'],
                        snippet=clean_snippet
                    )
                    db.session.add(event_entry)
            else:
                print(f"Failed to fetch data for {event}: {response.status_code}")
        db.session.commit()
        print("Data added successfully.")

if __name__ == '__main__':
    fetch_and_store_events()
