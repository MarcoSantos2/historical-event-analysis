# src/init_db.py
#script to initialize the database - BE CAREFUL, BEFORE RUNNING THIS SCRIPT BE SURE YOU ARE NOT DELETING ANYTHING OF RELEVANCE FROM YOUR TABLE

from app import app, db

with app.app_context():
    db.drop_all()  # Drop all tables
    db.create_all()  # Create tables based on the model

