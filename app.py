from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    # This will be replaced with actual data fetching from the database
    return jsonify([])

if __name__ == '__main__':
    app.run(debug=True)
