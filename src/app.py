# src/app.py
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import plotly.express as px
import plotly.io as pio
import pandas as pd
from io import StringIO

app = Flask(__name__, static_folder='../static', template_folder='../templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///history.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Discovery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False)
    date = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return f'<Discovery {self.name}>'

class EconomicData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer, nullable=False)
    gdp = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<EconomicData {self.year}>'

@app.route('/')
def home():
    # Query data from the database
    discoveries = Discovery.query.all()
    economic_data = EconomicData.query.all()

    # Convert data to DataFrames
    discovery_df = pd.DataFrame([{
        'name': d.name,
        'date': d.date,
        'category': d.category
    } for d in discoveries])
    economic_df = pd.DataFrame([{
        'year': e.year,
        'gdp': e.gdp
    } for e in economic_data])

    # Create a Plotly graph for cumulative discoveries
    discovery_df['date'] = pd.to_datetime(discovery_df['date'])
    discovery_df.sort_values(by='date', inplace=True)
    discovery_df['cumulative_discoveries'] = range(1, len(discovery_df) + 1)
    discovery_fig = px.line(discovery_df, x='date', y='cumulative_discoveries', title='Cumulative Discoveries Over Time')
    discovery_graph = pio.to_html(discovery_fig, full_html=False)

    # Create a Plotly graph for GDP growth
    gdp_fig = px.line(economic_df, x='year', y='gdp', title='GDP Growth Over Time')
    gdp_graph = pio.to_html(gdp_fig, full_html=False)

    # Combine both graphs into one for combined view
    combined_df = pd.merge_asof(discovery_df.sort_values('date'), economic_df.sort_values('year'), left_on='date', right_on='year')
    combined_fig = px.line(combined_df, x='date', y='cumulative_discoveries', title='Cumulative Discoveries and GDP Growth')
    combined_fig.add_scatter(x=combined_df['year'], y=combined_df['gdp'], mode='lines', name='GDP')
    combined_graph = pio.to_html(combined_fig, full_html=False)

    return render_template('index.html', discovery_graph=discovery_graph, gdp_graph=gdp_graph, combined_graph=combined_graph)

if __name__ == '__main__':
    app.run(debug=True)
