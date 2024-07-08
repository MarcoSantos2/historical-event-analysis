# src/init_db.py
#script to initialize the database

from app import app, db

with app.app_context():
    db.create_all()
