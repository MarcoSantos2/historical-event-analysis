# src/app.py
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

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
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)



# # src/app.py
# from flask import Flask, render_template
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

# app = Flask(__name__, static_folder='../static', template_folder='../templates')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///history.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)

# class Discovery(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(256), nullable=False)
#     date = db.Column(db.String(128), nullable=False)
#     description = db.Column(db.Text, nullable=False)
#     category = db.Column(db.String(128), nullable=False)

#     def __repr__(self):
#         return f'<Discovery {self.name}>'

# class EconomicData(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     year = db.Column(db.Integer, nullable=False)
#     gdp = db.Column(db.Float, nullable=False)

#     def __repr__(self):
#         return f'<EconomicData {self.year}>'

# @app.route('/')
# def home():
#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run(debug=True)
