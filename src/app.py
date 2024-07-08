# src/app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///events.db'  # For simplicity, using SQLite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), nullable=False)
    snippet = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Event {self.title}>'

@app.route('/')
def home():
    return "Hello, Flask!"

@app.route('/events')
def events():
    events = Event.query.all()
    return "<br>".join([f"{event.title}, {event.snippet}" for event in events])

if __name__ == '__main__':
    app.run(debug=True)

