# src/test_add_data.py
from app import app, db, Event

def add_sample_data():
    with app.app_context():
        # Sample data
        event1 = Event(name='Event One', date='2023-01-01', description='Description for event one.')
        event2 = Event(name='Event Two', date='2023-02-01', description='testing 123')
        
        # Add to the session
        db.session.add(event1)
        db.session.add(event2)
        
        # Commit the session
        db.session.commit()
        print("Data added successfully.")

if __name__ == '__main__':
    add_sample_data()
